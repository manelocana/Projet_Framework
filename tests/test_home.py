

def test_home_status_code(client):
    res = client.get("/")
    assert res.status_code == 200


def test_home_content(client):
    res = client.get("/")
    assert b"<html" in res.data
