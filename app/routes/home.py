from flask import Blueprint, render_template
from app.models.portfolio import Project


home_bp = Blueprint('home', __name__)



def get_projects():
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('home.html', projects=projects, title='Home')

def get_posts():
    posts = [
        {"title": "Primer Post", "image": "home_cards_1.jpeg", "url": "/post/1"},
        {"title": "Segundo Post", "image": "home_cards_2.jpeg", "url": "/post/2"},
        {"title": "Tercer Post", "image": "home_cards_3.jpeg", "url": "/post/3"},
    ]
    return render_template('home.html', posts=posts)


@home_bp.route('/')
def home():
    projects = get_projects()
    posts = get_posts()
    return render_template('home.html', projects=projects, posts=posts, title='Home')