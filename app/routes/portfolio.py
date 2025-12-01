from flask import Blueprint, render_template

portfolio_bp = Blueprint('portfolio', __name__)


@portfolio_bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', search_button=True)


@portfolio_bp.route('/portfolio/projet_1')
def projet_1():
    return render_template('portfolio/projet_1.html', search_button=True)


@portfolio_bp.route('/portfolio/projet1_photos')
def projet1_photos():
    return render_template('portfolio/projet1_photos.html', search_button=True)