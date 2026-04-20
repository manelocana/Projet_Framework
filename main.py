

from app import create_app
from app.extensions import db



""" simplement on lance la app """

app = create_app()



""" pour creer la premiere db , je fais comment ca, mais avec flask-migrate on ne l'utilise pas """
""" dans le dossier utils j'ai diferents scripts pour faire choses directement """

""" with app.app_context():
    db.create_all() """
    



""" en production le debug doit etre False, et on utilise gunicorn+gninx pour le deploy
debug=True seulement pour developper """

if __name__ == "__main__":
    app.run(debug=True)
