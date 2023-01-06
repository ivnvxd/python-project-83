from page_analyzer.app import app


def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert b"Page Analyzer" in response.data


# def test_urls_route():
#     response = app.test_client().get('/urls')
#     assert response.status_code == 200
#
#
# def test_random_url_route():
#     response = app.test_client().get('/urls/1')
#     assert response.status_code == 200
