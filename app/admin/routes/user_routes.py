


from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.decorators import role_required



user_bp = Blueprint("user", __name__, url_prefix="/user")


# Route de profil personnel
@user_bp.route("/profile")
@login_required
@role_required(["user", "admin"])
def profile():
    return render_template("user/profile.html", user=current_user)
