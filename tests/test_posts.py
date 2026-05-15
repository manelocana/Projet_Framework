

from app.models.post import Post



def test_create_post(client, login, admin_user, db):

    login(admin_user)

    response = client.post("/admin/blog/new", data={
        "title": "New post",
        "description": "Description pour le test",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"New post" in response.data

    post = db.session.query(Post).filter_by(title="New post").first()
    assert post is not None




def test_normal_user_cannot_create_post(login, client, user):

    login(user)

    response = client.post("/admin/blog/new", data={
        "title": "premier essai",
        "description": "je ne suis pas admin"
    })

    assert response.status_code in (302, 403)





def test_create_post_empty_title(login, client, admin_user):

    login(admin_user)

    response = client.post("/admin/blog/new", data={
        "title": "title pour create",
        "description": "Texte"
    })

    assert response.status_code == 200
    assert b"error" in response.data.lower()








def test_edit_post(login, client, admin_user, post, db):

    login(admin_user)

    response = client.post(f"/admin/blog/{post.id}/edit", data={
        "title": "Modifier",
        "description": "New text"
    }, follow_redirects=True)

    assert response.status_code == 200

    updated = db.session.get(Post, post.id)

    assert updated.title == "Modifié"





def test_delete_post(login, client, admin_user, post, db):

    login(admin_user)

    response = client.post(
        f"/admin/blog/{post.id}/delete",
        follow_redirects=True
    )

    assert response.status_code == 200

    deleted = db.session.get(Post, post.id)

    assert deleted is None



