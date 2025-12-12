

from flask import Blueprint, render_template
from app.models.post import Post



blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/blog')
def blog():
    return render_template('blog.html', search_button=True)


@blog_bp.route('/blog/article')
def blog_article():
    return render_template('blog/article.html', search_button=True)


@blog_bp.route('/blog/list')
def list_posts():
    posts = Post.query.all()
    return render_template('blog/list.html', posts=posts)