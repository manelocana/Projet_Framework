
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from werkzeug.security import check_password_hash
from app.extensions import login_manager


from urllib.parse import urlparse, urljoin



auth_bp = Blueprint('auth', __name__, template_folder='../templates')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')
            if next_page and is_safe_url(next_page):
                return redirect(next_page)

            return redirect(url_for('home.home'))

        flash('Pass or name not correct', 'error')

    return render_template('admin/auth/login.html')



@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))




