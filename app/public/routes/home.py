

from flask import Blueprint, render_template
from app.models.portfolio import Project
from app.models.post import Post



""" POUR PAS FAIRE TOUTES LES ROUTES DANS LE MEME FICHIER, JE FAIS DES BLUEPRINTS """



""" home_bp pour pouvoir appeler a la route avec son decorateur
ici le nom del blueprint c'est 'home' , tres important apres pour creer les routes,
dans le dossier templates """
home_bp = Blueprint('home', __name__, template_folder='../templates')



""" metodes pour appeler a mysql avec query, avec des filtres """
def get_projects():
    return Project.query.order_by(Project.id.desc()).all()

def get_posts(limit=3):
    return Post.query.order_by(Post.id.desc()).limit(limit).all()



""" route pour monstrer le home, avec le metode 'home' et les variables avec les donnes de mysql """ 
@home_bp.route('/')
def home():
    projects = get_projects()
    posts = get_posts()

    """ avec jinja je envoi les variables directement a html """
    return render_template('public/home.html', projects=projects, posts=posts, title='Home')