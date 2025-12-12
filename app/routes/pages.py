from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__)


@pages_bp.route('/pages')
def pages():
    return render_template('pages.html', search_button=True)


@pages_bp.route('/pages/branding')
def branding():
    return render_template('services/projet_branding.html', search_button=True)

