from app.models.post import Post


def login(client, user):
    with client.session_transaction() as sess:
        sess["_user_id"] = str(user.id)


def test_create_post(client, admin_user, db):
    login(client, admin_user)

    response = client.post("/admin/blog/new", data={
        "title": "Nuevo post",
        "description": "Descripción de prueba",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Nuevo post" in response.data

    post = db.session.query(Post).filter_by(title="Nuevo post").first()
    assert post is not None