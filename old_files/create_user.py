


from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash

user = User(
    username="user",
    password=generate_password_hash("1234"),
    role="user"
)

db.session.add(user)
db.session.commit()

print("User created")
