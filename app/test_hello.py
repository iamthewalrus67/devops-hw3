from hello import app


def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert 4 == 4
    # more and more tests to be here
