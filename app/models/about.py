

from app.extensions import db


""" table about, y pas de relation, car il aurait que une """

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

