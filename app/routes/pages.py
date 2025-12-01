from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__)


@pages_bp.route('/pages')
def pages():
    return render_template('pages.html', search_button=True)


@pages_bp.route('/pages/projet_1')
def projet_1():
    return render_template('projet_1.html', search_button=True)


@pages_bp.route('/pages/branding')
def branding():
    return render_template('projet_branding.html', search_button=True)


@pages_bp.route('/pages/projet1_photos')
def projet1_photos():
    return render_template('projet1_photos.html', search_button=True)