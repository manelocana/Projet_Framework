

from flask import Blueprint, render_template
from app.models.portfolio import Project



portfolio_bp = Blueprint('portfolio', __name__, template_folder='../templates')




@portfolio_bp.route('/portfolio/projects/<string:page>')
def portfolio_static_project(page):
    return render_template(f'public/portfolio/{page}.html')


@portfolio_bp.route('/portfolio')
def portfolio():
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('public/portfolio/portfolio.html', projects=projects)


@portfolio_bp.route('/portfolio/<int:project_id>')
def portfolio_project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('public/portfolio/portfolio_project.html', project=project)