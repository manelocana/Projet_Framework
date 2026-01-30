


def test_blog_page(client):
    res = client.get("/blog")
    assert res.status_code == 200


def test_portfolio_page(client):
    res = client.get("/portfolio")
    assert res.status_code == 200


def test_about_page(client):
    res = client.get("/pages")
    assert res.status_code == 200