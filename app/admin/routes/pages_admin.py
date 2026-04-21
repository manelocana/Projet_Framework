

from flask import Blueprint, render_template, redirect, url_for, flash
from app.models.about import About
from app.extensions import db
from flask_login import login_required
from app.forms.about import AboutForm

from app.decorators import role_required

from flask_login import current_user




pages_admin_bp = Blueprint('admin_pages', __name__, template_folder='../templates/admin/pages')




@pages_admin_bp.route('/about/edit', methods=['GET', 'POST'])
@login_required
@role_required(['admin'])

def edit_about():

    about = About.query.first()

    if not about:
        try:
            about = About(content="")
            db.session.add(about)
            db.session.commit()
        
        except Exception as e:
            db.session.rollback()
            flash('erreur about', 'danger')
            print(str(e))

    form = AboutForm(obj=about)

    if form.validate_on_submit():

        try:
            about.content = form.content.data   # --> html ckeditor
            db.session.commit()
            return redirect(url_for('pages.pages'))
        
        except Exception as e:
            db.session.rollback()
            flash('erreur al modifier', 'danger')
            print(str(e))
    
    return render_template('admin/pages/about_edit.html', form=form, about=about)