

# Portfolio Artiste - Project web Formation Ilaria Digital School


## Application web développée avec Flask comprenant un portfolio de projets, un blog, ainsi qu’un espace d’administration sécurisé permettant de créer, modifier et supprimer du contenu.

### Ce projet sert de base/template pour un portfolio personnel ou pour des sites web de petits clients.

- Fonctionnalités
- Partie publique


### --> Le site est composé de:

Page d’accueil

Page about, avec la description de l'artiste 

Portfolio avec liste de projets

Page détaillée pour chaque projet

Blog avec articles

Page individuelle pour chaque article

Une page pour contact



### --> Administration (connexion requise)

Connexion / Déconnexion administrateur


CRUD complet :

Projets (portfolio)

Articles (blog)

Modification et suppression du contenu


Upload d’images pour :
les projets
les articles


### --> Technologies utilisées

Python 3

Flask

Flask-SQLAlchemy

Flask-Login

Jinja2

SQLite (environnement local) --> pour tester sqlite3, jamais utilisé avant, je trouve un peu perdre le temps,
                                meilleur utiliser mysql directement, et faire des migrations pour les changements de models

MySQL - pymysql - 

HTML5 / CSS3

JavaScript

Werkzeug (secure_filename)


### --> Structure du projet

```
Projet_Framework/
│
├── app/
│   ├── __init__.py
|   |
│   ├── extensions.py
|   |
|   ├── forms/
│   │   ├── admin.py
│   │   ├── about.py
│   │   └── portfolio.py
|   |
│   ├── models/
│   │   ├── user.py
│   │   ├── post.py
│   │   └── portfolio.py
│   │
│   ├── admin routes/
│   │   ├── auth.py
│   │   ├── blog.py
│   │   ├── contact.py
│   │   ├── home.py
│   │   ├── pages.py
│   │   └── portfolio.py
│   │       
|   ├── public routes/
│   │   ├── blog.py
│   │   ├── contact.py
│   │   ├── home.py
│   │   ├── pages.py
│   │   └── portfolio.py
│   │
│   ├── templates/
│   │   ├── admin/
│   │   ├── partials/
│   │   ├── public/
│   │   └── user/
│   │
|   ├── utils/
│   │   └── scripts.py
|   |
│   └── static/
│       ├── css/
│       ├── img/
│       └── uploads/
│           ├── blog/
│           └── portfolio/
│
├── instance/
│   └── portfolio.db (SQLITE3)
│
|
├── .env
├── config.py
├── main.py
├── requirements.txt
└── README.md
```



### --> Installation

- Cloner le projet
  
git clone <url-du-repo>

cd Projet_Framework

- Créer un environnement virtuel
 
python -m venv venv

source venv/bin/activate

- Installer les dépendances
 
pip install -r requirements.txt

- Base de données
  
Base de données utilisée a debut : SQLite

Fichier : instance/portfolio.db

ORM : SQLAlchemy

Les modèles principaux sont :

  User
  Project
  Post

Aprés, changement a base de données MySQL avec sqlalchemy + pymysql


### --> Authentification

Accès administrateur protégé avec Flask-Login

Les routes de création / édition / suppression sont protégées par :

@login_required

Exemple :

/portfolio/new

/blog/new

/portfolio/<id>/edit

/blog/<id>/edit



### --> Upload d’images

Les images uploadées sont stockées dans :

```
  app/static/uploads/
  ├── blog/
  └── portfolio/
``` 


Les noms de fichiers sont sécurisés avec :

secure_filename()


### --> Sécurité

Authentification requise pour les routes d’administration
secure_filename pour les uploads

Fichiers sensibles exclus du dépôt :

instance/

fichiers .db

venv/




Configuration prête pour variables d’environnement (SECRET_KEY)

### --> Lancement du projet <--

python main.py


Puis ouvrir :

http://127.0.0.1:5000


### --> Remarques

Projet conçu selon une architecture MVC simple

Code organisé avec Blueprints

Base solide pour des évolutions futures :

Flask-WTF pour les formulaires (securité)



## Philosophie du Projet

- Backend : Flask
- ORM : SQLAlchemy
- Base de données : MySQL (production dès le départ)
- Authentification : Flask-Login
- Formulaires : Flask-WTF
- Frontend : HTML + CSS (Mobile First)
- Architecture modulaire : Blueprints
- Fonctionnalités : CRUD complet, admin sécurisé, upload d’images, UI dynamique selon la session

--- 

## Préparation du Projet

Créer le répertoire et l’environnement virtuel :

  ```
  mkdir mon_projet
  cd mon_projet
  python -m venv venv
  ```

### Activer le venv
### Windows : venv\Scripts\activate
### Mac/Linux : source venv/bin/activate


### Installer les dépendances :

  pip install flask flask_sqlalchemy flask_login flask_wtf flask_migrate pymysql python-dotenv

### Enregistrer les dépendances :

  pip freeze > requirements.txt

### Créer le fichier .gitignore avec:

  venv/
  __pycache__/
  instance/
  .env


---


## Configuration de Base pour MySQL

📍 config.py

```
import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:password@localhost/ma_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'uploads')

```


- Remplace root:password@localhost/ma_db par tes vraies informations MySQL
- Tu peux utiliser .env pour éviter d’exposer les mots de passe :
- DATABASE_URL=mysql+pymysql://root:1234@localhost/ma_db
- SECRET_KEY=supersecrete


---


## Extensions

📍 app/extensions.py

```
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
login_manager = LoginManager()
```

---



##  Création de l’Application

# app/init.py

```
from flask import Flask
from config import Config
from app.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.routes.public import public_bp
    from app.routes.admin import admin_bp
    from app.routes.user import user_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
```



# main.py

```
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

---



## Création de la Base de Données MySQL

- Dans MySQL :

```
CREATE DATABASE ma_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'utilisateur'@'localhost' IDENTIFIED BY 'mot_de_passe';
GRANT ALL PRIVILEGES ON ma_db.* TO 'utilisateur'@'localhost';
FLUSH PRIVILEGES;
```


- Configurer .env :
  DATABASE_URL=mysql+pymysql://utilisateur:mot_de_passe@localhost/ma_db

---

## Migrations avec Flask-Migrate

```
flask db init
flask db migrate -m "Schéma initial"
flask db upgrade
```

---



##  Modèles

📍 app/models/user.py

```
from app.extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
```



📍 app/models/project.py

```
from app.extensions import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200))
```


---



## Flask-Login


📍 auth.py

```
from app.extensions import login_manager
from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

---



## CRUD Basique


- Lister les projets :

```
@portfolio_bp.route('/')
def portfolio():
    projects = Project.query.all()
    return render_template('portfolio.html', projects=projects)
```


- Créer un projet :

```
@portfolio_bp.route('/new', methods=['GET','POST'])
@login_required
def new_project():
    if request.method == 'POST':
        # Sauvegarder en DB
        pass
```

---


## Upload d’Images

Formulaire :

  <form method="POST" enctype="multipart/form-data">

Backend :

```
from werkzeug.utils import secure_filename
import os

image_file = request.files.get('image')

if image_file and image_file.filename:
    filename = secure_filename(image_file.filename)
    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'portfolio')
    os.makedirs(upload_path, exist_ok=True)
    image_file.save(os.path.join(upload_path, filename))
```


Template :
  <img src="{{ url_for('static', filename='uploads/portfolio/' ~ project.image) }}">


---


## Suppression d’Images


  if project.image:
      os.remove(image_path)


---


## Protection des Routes

  from flask_login import login_required

  @login_required
  def admin_panel():
    ...


---


## UI Dynamique

```
{% if current_user.is_authenticated %}
    <a href="{{ url_for('auth.logout') }}">Logout</a>
{% else %}
    <a href="{{ url_for('auth.login') }}">Login</a>
{% endif %}
```


---



## Création d’un Admin

```
flask shell
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.user import User

admin = User(username="admin", password=generate_password_hash("1234"))
db.session.add(admin)
db.session.commit()
```

---



## Bonnes Pratiques

- Séparer les uploads (uploads/portfolio/, uploads/blog/)
- Toujours utiliser secure_filename()
- Utiliser os.makedirs(..., exist_ok=True)
- Mobile First, CSS réutilisable
- Un blueprint par fonctionnalité
- Backup de la base avant production
- Fichiers CSS/JS locaux si offline