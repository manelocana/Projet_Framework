


from flask import Blueprint, render_template, request, redirect, url_for
from app.models.post import Post
from app.extensions import db
from flask_login import login_required
from app.forms.blog import BlogForm

from app.utils.image_utils import save_image, delete_image



blog_admin_bp = Blueprint('blog_admin', __name__, template_folder='../templates', url_prefix='/admin')



@blog_admin_bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
def blog_new():
    form = BlogForm()

    if form.validate_on_submit():
        image_file = request.files.get('image')
        image_filename = save_image(image_file, 'blog')
        
        new_post = Post(title=form.title.data,
                        content=form.content.data, 
                        image=image_filename)

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('blog.blog'))
    return render_template('admin/blog/blog_new.html', form=form)




@blog_admin_bp.route('/blog/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def blog_edit(post_id):
    post = Post.query.get_or_404(post_id)
    form = BlogForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data

        # voir si on monte le img
        image_file = request.files.get('image')
        if image_file and image_file.filename:
            delete_image(post.image, 'blog')
            post.image = save_image(image_file, 'blog')

        db.session.commit()

        return redirect(url_for('blog.blog_article', post_id=post.id))
    return render_template('admin/blog/blog_edit.html', form=form)




@blog_admin_bp.route('/blog/<int:post_id>/delete', methods=['POST'])
@login_required
def blog_delete(post_id):
    post = Post.query.get_or_404(post_id)

    delete_image(post.image, 'blog')

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blog.blog'))
