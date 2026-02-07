


from flask import Blueprint, render_template
from flask_login import login_required
from app.decorators import role_required

from app.models.user import User




admin_bp = Blueprint("admin", __name__, template_folder='../templates')





@admin_bp.route("/admin")
@login_required
@role_required(["admin"])
def admin_dashboard():
    return render_template("admin/administration/dashboard.html")




@admin_bp.route('/admin/users')
@login_required
@role_required(['admin'])
def admin_users():
    users = User.query.order_by(User.id.asc()).all()
    return render_template('admin/administration/users.html', users=users)