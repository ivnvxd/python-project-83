from page_analyzer.app import app


def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Welcome!'
    assert b"Welcome" in response.data
