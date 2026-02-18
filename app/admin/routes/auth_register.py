


from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.user import User
from flask_login import current_user

from app.forms.auth import RegisterForm



auth_register_bp = Blueprint('auth_register', __name__)



@auth_register_bp.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if current_user.is_authenticated:
        return redirect(url_for('home.home'))

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if not username or not password:
            flash("All field required", "error")
            return redirect(url_for('auth_register.register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("user exist", "error")
            return redirect(url_for('auth_register.register'))

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("user created ok, u can login.", "success")
        return redirect(url_for('auth.login'))

    return render_template('admin/auth/register.html', form=form)
