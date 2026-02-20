


# test a la pagina home 
def test_home_page(client):
    """Test que la página de inicio carga correctamente"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"home" in response.data  # Cambia esto segun template


# comprobamos la  redirecion si no es admin
def test_dashboard_requires_login(app):
    """Test que la página del dashboard requiere login"""
    
    with app.app_context():
        with app.test_client() as client:
            response = client.get("/admin/")
            # Redirige al login si no esta autenticado
            assert response.status_code == 302
            assert "/login" in response.location


# test para ver si admin puede acceder a /admin (el dashboard)
def test_dashboard_logged_in(client, admin_user, app):
    """Test que un usuario logueado puede acceder al dashboard"""
    from flask_login import login_user

    with app.app_context():
        # Logueamos al usuario manualmente
        from flask_login import login_user
        from app.extensions import login_manager

        # Necesitamos un request context para usar login_user
        with app.test_request_context():
            login_user(admin_user)
            response = client.get("/admin/")
            assert response.status_code == 200
            assert b"/admin" in response.data  # Cambia segun template
