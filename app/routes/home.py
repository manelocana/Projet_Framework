from flask import Blueprint, render_template
from app.models.portfolio import Project


home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def home():
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('home.html', projects=projects, title='Home')