

from app import create_app
from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash



app = create_app()
with app.app_context():
    admin = User(username="admin", password=generate_password_hash("1234"), role="admin")
    db.session.add(admin)
    db.session.commit()
    print("User admin created")
