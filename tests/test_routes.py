


# test page home 
def test_home_page(client):
    """Test que la página de inicio carga correctamente"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"home" in response.data  # ca depends del template


# test redirections , quand il est pas admin
def test_dashboard_requires_login(app):
    """pour tester le panel admin"""
    
    with app.app_context():
        with app.test_client() as client:
            response = client.get("/admin/")
            # redirection a login , si nest pas admin
            assert response.status_code == 302
            assert "/login" in response.location


# test pour voir si admin peut entrer au panel admin /admin
def test_dashboard_logged_in(client, admin_user, app):
    from flask_login import login_user

    with app.app_context():
        # loggin user
        from flask_login import login_user

        # creation de request contetst pour utiliser le login_user
        with app.test_request_context():
            login_user(admin_user)
            response = client.get("/admin/")
            assert response.status_code == 200
            assert b"/admin" in response.data  # ça depends le template , on peu le changer
