

from flask import Blueprint, render_template
from app.models.about import About


pages_bp = Blueprint('pages', __name__, template_folder='../templates/public/pages')




@pages_bp.route('/pages')
def pages():
    about = About.query.first()
    return render_template('public/pages/pages.html', about=about)


@pages_bp.route('/pages/projet_branding')
def branding():
    return render_template('public/pages/projet_branding.html')


