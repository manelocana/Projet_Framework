

from flask import Blueprint, render_template, request, redirect, url_for
from app.models.post import Post
from app.extensions import db



blog_bp = Blueprint('blog', __name__)


""" @blog_bp.route('/blog')
def blog():
    return render_template('blog/blog.html', search_button=True) """


""" @blog_bp.route('/blog/article')
def blog_article():
    return render_template('blog/blog_article.html', search_button=True) """


@blog_bp.route('/blog')
def blog():
    posts = Post.query.all()
    return render_template('blog/blog.html', posts=posts)


@blog_bp.route('/blog/<int:post_id>')
def blog_article(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/blog_article.html', post=post)


@blog_bp.route('/blog/new', methods=['GET', 'POST'])
def blog_new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('blog.blog'))

    return render_template('blog/blog_new.html')