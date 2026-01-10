Portfolio Artiste - Project web Formation Ilaria Digital School


Application web développée avec Flask comprenant un portfolio de projets, un blog, ainsi qu’un espace d’administration sécurisé permettant de créer, modifier et supprimer du contenu.

Ce projet sert de base/template pour un portfolio personnel ou pour des sites web de petits clients.

- Fonctionnalités
- Partie publique

- Le site est composé de: 
Page d’accueil
Portfolio avec liste de projets
Page détaillée pour chaque projet
Blog avec articles
Page individuelle pour chaque article


--> Administration (connexion requise)

Connexion / Déconnexion administrateur

CRUD complet :
Projets (portfolio)
Articles (blog)
Modification et suppression du contenu

Upload d’images pour :
les projets
les articles


--> Technologies utilisées

Python 3
Flask
Flask-SQLAlchemy
Flask-Login
Jinja2
SQLite (environnement local) --> Aprés je ferais des migrations
HTML5 / CSS3
JavaScript
Werkzeug (secure_filename)

--> Structure du projet

```
Projet_Framework/
│
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models/
│   │   ├── user.py
│   │   ├── post.py
│   │   └── portfolio.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── blog.py
│   │   ├── contact.py
│   │   ├── home.py
│   │   ├── pages.py
│   │   └── portfolio.py
│   │       
│   │
│   ├── templates/
│   │   ├── blog/
│   │   ├── portfolio/
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       ├── img/
│       └── uploads/
│           ├── blog/
│           └── portfolio/
│
├── instance/
│   └── portfolio.db
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```



--> Installation

- Cloner le projet
git clone <url-du-repo>
cd Projet_Framework

- Créer un environnement virtuel
python -m venv venv
source venv/bin/activate

- Installer les dépendances
pip install requirements.txt

- Base de données
Base de données utilisée : SQLite
Fichier : instance/portfolio.db
ORM : SQLAlchemy
Les modèles principaux sont :
  User
  Project
  Post


--> Authentification

Accès administrateur protégé avec Flask-Login
Les routes de création / édition / suppression sont protégées par :
@login_required
Exemple :
/portfolio/new
/blog/new
/portfolio/<id>/edit
/blog/<id>/edit

--> Upload d’images
Les images uploadées sont stockées dans :
  app/static/uploads/
  ├── blog/
  └── portfolio/


Les noms de fichiers sont sécurisés avec :
secure_filename()


--> Sécurité

Authentification requise pour les routes d’administration
secure_filename pour les uploads

Fichiers sensibles exclus du dépôt :
instance/
fichiers .db
venv/
Configuration prête pour variables d’environnement (SECRET_KEY)

--> Lancement du projet <--
python main.py


Puis ouvrir :
http://127.0.0.1:5000


--> Remarques

Projet conçu selon une architecture MVC simple
Code organisé avec Blueprints
Base solide pour des évolutions futures :
Flask-WTF
MySQL
AJAX / Fetch


