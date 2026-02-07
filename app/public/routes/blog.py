

from flask import Blueprint, render_template
from app.models.post import Post




blog_bp = Blueprint('blog', __name__, template_folder='../templates')





@blog_bp.route('/blog')
def blog():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('public/blog/blog.html', posts=posts)


@blog_bp.route('/blog/<int:post_id>')
def blog_article(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('public/blog/blog_article.html', post=post)


