

from app.extensions import db


""" table post msyql """
""" colum, integer , pk , langague pour mysql """
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))

    """ relation post => user_id """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)