

def test_admin_user_exists(admin_user):
    assert admin_user.username == "admin"
