

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.portfolio import Project
from app.extensions import db
from werkzeug.utils import secure_filename
from flask_login import login_required

from app.forms.portfolio import PortfolioForm
from app.utils.image_utils import save_image, delete_image
from app.decorators import role_required




portfolio_admin_bp = Blueprint('portfolio_admin', __name__, template_folder='../templates', url_prefix='/admin')





@portfolio_admin_bp.route('/portfolio')
@login_required
@role_required(["admin"])
def portfolio_admin_list():
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('admin/portfolio/portfolio_list.html', projects=projects)



@portfolio_admin_bp.route('/portfolio/new', methods=['GET', 'POST'])
@login_required
@role_required(["admin"])
def portfolio_new():
    form = PortfolioForm()

    if form.validate_on_submit():
        image_file = request.files.get('image')
        image_filename = save_image(image_file, 'portfolio')

        new_project = Project(
            title=form.title.data,
            description=form.description.data,
            image=image_filename
        )

        db.session.add(new_project)
        db.session.commit()
                
        flash("Project added successfully!", "success")

        return redirect(url_for('portfolio_admin.portfolio_admin_list'))
    
    if form.errors:
        print(form.errors)

    return render_template('admin/portfolio/portfolio_new.html', form=form)



@portfolio_admin_bp.route('/portfolio/<int:project_id>/edit', methods=['GET', 'POST'])
@login_required
@role_required(["admin"])
def portfolio_edit(project_id):
    project = Project.query.get_or_404(project_id)
    """ para que edit tenga los valores ya puestos """
    form = PortfolioForm(obj=project)

    if form.validate_on_submit():
        """ actualizar datos """
        project.title = form.title.data
        project.description = form.description.data

        image_file = request.files.get('image')
        if image_file and image_file.filename:
            delete_image(project.image, 'portfolio')
            project.image = save_image(image_file, 'portfolio')

        db.session.commit()

        flash("Project added successfully!", "success")

        return redirect(url_for('portfolio_admin.portfolio_admin_list'))

    return render_template('admin/portfolio/portfolio_edit.html', form=form, project=project)



@portfolio_admin_bp.route('/portfolio/<int:project_id>/delete', methods=['POST'])
@login_required
@role_required(["admin"])
def portfolio_delete(project_id):
    project = Project.query.get_or_404(project_id)

    delete_image(project.image, 'portfolio')

    db.session.delete(project)
    db.session.commit()

    flash("Project delete successfully!", "danger")

    return redirect(url_for('portfolio_admin.portfolio_admin_list'))
