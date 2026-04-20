

from app.extensions import db


""" table mysql project, pour le portfolio """
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))

    """ relation """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)