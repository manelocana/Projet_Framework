


from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.forms.user import EditProfileForm, ChangePasswordForm




user_bp = Blueprint("user", __name__, template_folder="../../templates", url_prefix="/user")




@user_bp.route("/profile")
@login_required
def profile():
    return render_template("user/profile.html", user=current_user)




@user_bp.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user)

    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash("Profile updated successfully", "success")
        return redirect(url_for("user.profile"))

    return render_template("user/edit_profile.html", form=form)





@user_bp.route("/profile/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():

        if not check_password_hash(current_user.password, form.old_password.data):
            flash("Current password is incorrect", "danger")
            return redirect(url_for("user.change_password"))

        current_user.password = generate_password_hash(form.new_password.data)
        db.session.commit()

        flash("Password updated successfully", "success")
        return redirect(url_for("user.profile"))

    return render_template("user/change_password.html", form=form)
