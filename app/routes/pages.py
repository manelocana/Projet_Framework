from flask import Blueprint, render_template, url_for, redirect
from app.extensions import db
from flask_login import login_required
from app.models.about import About
from app.forms.about import AboutForm


pages_bp = Blueprint('pages', __name__)


""" @pages_bp.route('/pages')
def pages():
    return render_template('pages.html', search_button=True) """

""" @pages_bp.route('/pages')
def pages():
    about = About.query.first()
    if not about:
        about = About(content="")
    return render_template('pages.html', about=about, search_button=True) """

@pages_bp.route('/pages')
def pages():
    about = About.query.first()
    return render_template('pages.html', about=about)


@pages_bp.route('/pages/projet_branding')
def branding():
    return render_template('pages/projet_branding.html', search_button=True)


@pages_bp.route('/about/edit', methods=['GET', 'POST'])
@login_required
def edit_about():
    about = About.query.first()
    if not about:
        about = About(content="")
        db.session.add(about)
        db.session.commit()

    form = AboutForm(obj=about)

    if form.validate_on_submit():
        about.content = form.content.data
        db.session.commit()
        return redirect(url_for('pages.pages'))

    return render_template('pages/about_edit.html', form=form)