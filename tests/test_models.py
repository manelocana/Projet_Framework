

from app.models.user import User



def test_create_user(db):

    user = User(username="pepe", password="1234")

    db.session.add(user)
    db.session.commit()

    assert user.id is not None




def test_password_is_hashed(user):

    assert user.password != "1234"