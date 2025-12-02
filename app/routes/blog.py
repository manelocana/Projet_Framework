from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/blog')
def blog():
    return render_template('blog.html', search_button=True)


@blog_bp.route('/blog/article')
def blog_article():
    return render_template('landing_blog.html', search_button=True)
