from flask import Blueprint, render_template, request, redirect, url_for
from app.models.portfolio import Project
from app.extensions import db


portfolio_bp = Blueprint('portfolio', __name__)

# routes static, for starting test
""" @portfolio_bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', search_button=True)

@portfolio_bp.route('/portfolio/projet_1')
def projet_1():
    return render_template('portfolio/projet_1.html', search_button=True)

@portfolio_bp.route('/portfolio/projet1_photos')
def projet1_photos():
    return render_template('portfolio/projet1_photos.html', search_button=True) """


@portfolio_bp.route('/portfolio')
def portfolio():
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('portfolio/portfolio.html', projects=projects)


@portfolio_bp.route('/portfolio/<int:project_id>')
def portfolio_project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('portfolio/portfolio_project.html', project=project)


@portfolio_bp.route('/portfolio/new', methods=['GET', 'POST'])
def portfolio_new():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        new_project = Project(title=title, description=description, image=image)

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('portfolio.portfolio'))
    return render_template('portfolio/portfolio_new.html')


@portfolio_bp.route('/portfolio/<int:project_id>/edit', methods=['GET', 'POST'])
def portfolio_edit(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.image = request.form['image']

        db.session.commit()
        return redirect(url_for('portfolio.portfolio_project', project_id=project.id))
    return render_template('portfolio/portfolio_edit.html', project=project)


@portfolio_bp.route('/portfolio/<int:project_id>/delete', methods=['POST'])
def portfolio_delete(project_id):
    project = Project.query.get_or_404(project_id)

    db.session.delete(project)
    db.session.commit()

    return redirect(url_for('portfolio.portfolio'))