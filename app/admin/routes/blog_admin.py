


from flask import Blueprint, render_template, redirect, url_for, flash
from app.models.post import Post
from app.extensions import db
from flask_login import login_required
from app.forms.blog import BlogForm

from app.utils.image_utils import save_image, delete_image
from app.decorators import role_required



blog_admin_bp = Blueprint('blog_admin', __name__, template_folder='../templates', url_prefix='/admin')




@blog_admin_bp.route('/blog')
@login_required
@role_required(["admin"])

def blog_list():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('admin/blog/blog_list.html', posts=posts)



@blog_admin_bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
@role_required(["admin"])
def blog_new():
    form = BlogForm()

    if form.validate_on_submit():
        image_file = form.image.data
        image_filename = save_image(image_file, 'blog')

        new_post = Post(
            title=form.title.data,
            description=form.description.data,
            image=image_filename
        )

        db.session.add(new_post)
        db.session.commit()
                
        flash("Post added successfully!", "success")

        return redirect(url_for('blog_admin.blog_list'))
    
    if form.errors:
        print(form.errors)

    return render_template('admin/blog/blog_new.html', form=form)



@blog_admin_bp.route('/blog/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
@role_required(["admin"])
def blog_edit(post_id):
    post = Post.query.get_or_404(post_id)
    """ para que edit tenga los valores ya puestos """
    form = BlogForm(obj=post)

    if form.validate_on_submit():
        """ actualizar datos """
        post.title = form.title.data
        post.description = form.description.data

        image_file = form.image.data
        if image_file and image_file.filename:
            delete_image(post.image, 'blog')
            post.image = save_image(image_file, 'blog')

        db.session.commit()

        flash("Post added successfully!", "success")

        return redirect(url_for('blog_admin.blog_list'))

    return render_template('admin/blog/blog_edit.html', form=form, post=post)



@blog_admin_bp.route('/blog/<int:post_id>/delete', methods=['POST'])
@login_required
@role_required(["admin"])
def blog_delete(post_id):
    post = Post.query.get_or_404(post_id)

    delete_image(post.image, 'blog')

    db.session.delete(post)
    db.session.commit()

    flash("Post delete successfully!", "danger")

    return redirect(url_for('blog_admin.blog_list'))
