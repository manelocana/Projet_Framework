


from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.decorators import role_required

from app.models.user import User
from app.extensions import db
from app.forms.admin import DeleteForm





admin_bp = Blueprint("admin", __name__, template_folder='../templates', url_prefix='/admin')





@admin_bp.route("/")
@login_required
@role_required(["admin"])
def admin_dashboard():
    return render_template("admin/administration/dashboard.html")




@admin_bp.route('/users')
@login_required
@role_required(['admin'])
def admin_users():
    users = User.query.order_by(User.id.asc()).all()
    delete_form = DeleteForm()
    return render_template('admin/administration/users.html', users=users, delete_form=delete_form)




@admin_bp.route("/users/<int:user_id>/delete", methods=["POST"])
@login_required
@role_required(["admin"])
def delete_user(user_id):

    user = User.query.get_or_404(user_id)

    # No permitir borrarse a sí mismo
    if user.id == current_user.id:
        flash("You cannot delete yourself.", "danger")
        return redirect(url_for("admin.admin_users"))

    # Contar admins
    admin_count = User.query.filter_by(role="admin").count()

    if user.role == "admin" and admin_count <= 1:
        flash("Cannot delete the last admin.", "danger")
        return redirect(url_for("admin.admin_users"))

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully.", "success")
    return redirect(url_for("admin.admin_users"))
