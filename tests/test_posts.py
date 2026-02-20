

from app.models.post import Post



def test_create_post(client, admin_user, app, db):
    """Test crear un post vía POST"""

    with app.test_request_context():
        from flask_login import login_user
        login_user(admin_user)

        response = client.post("/admin/blog/new", data={
            "title": "Nuevo post",
            "description": "Descripción de prueba"
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b"Nuevo post" in response.data

        # Comprobamos en la DB
        post = db.session.query(Post).filter_by(title="Nuevo post").first()
        assert post is not None
