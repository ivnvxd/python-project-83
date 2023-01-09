import pytest
from page_analyzer.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_index_route(client):
    response = client.get('/')
    html = response.data.decode()

    assert response.status_code == 200

    assert '<p class="lead">Бесплатно проверяйте сайты на SEO пригодность</p>' in html

    assert '<a class="navbar-brand" href="/">Анализатор страниц</a>' in html
    assert '<a class="nav-link " href="/urls">Сайты</a>' in html


def test_404(client):
    response = client.get('/qwerty')
    html = response.data.decode()

    assert response.status_code == 404

    assert '<h1>Страница не найдена</h1>' in html
