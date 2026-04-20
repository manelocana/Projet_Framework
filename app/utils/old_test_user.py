
from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash("1234")
admin = User(username="admin", password=hashed_password)

db.session.add(admin)
db.session.commit()
