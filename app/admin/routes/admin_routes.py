

""" modules pour flask """
from flask import Blueprint, render_template, redirect, url_for, flash

""" authentication avec flask_login """
from flask_login import login_required, current_user

""" script avec decorateur pour les roles """
from app.decorators import role_required

""" model et module de mysql """
from app.models.user import User
from app.extensions import db

""" wtforms pour le formulaire """
from app.forms.admin import DeleteForm


""" instance del blueprint, pour les routes admin """
admin_bp = Blueprint("admin", __name__, template_folder='../templates', url_prefix='/admin')


""" route get panel admin """
@admin_bp.route("/")
@login_required
@role_required(["admin"])
def admin_dashboard():
    """ render_template (flask) pour afficher directement a html """
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

    """ validation pour voir si y a un user, sinon lance un error 404 """
    user = User.query.get_or_404(user_id)

    """ pour pas ce supprimer a lui meme comment admin """
    if user.id == current_user.id:
        flash("You cannot delete yourself.", "danger")
        return redirect(url_for("admin.admin_users"))

    """ conter le numero de admins """
    admin_count = User.query.filter_by(role="admin").count()

    if user.role == "admin" and admin_count <= 1:
        flash("Cannot delete the last admin.", "danger")
        return redirect(url_for("admin.admin_users"))

    try:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully.", "success")

    except Exception as e:
        db.session.rollback()
        flash('erreur supprimer user', 'danger')
        print(str(e))

    return redirect(url_for("admin.admin_users"))
