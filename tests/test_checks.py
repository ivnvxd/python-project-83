import pytest
from requests import RequestException
from page_analyzer.checks import validate_url, get_url_data


@pytest.fixture()
def site():
    urls = {}
    urls['zero'] = {'url': '', 'error': 'zero'}
    urls['invalid'] = {'url': 'url.com', 'error': 'invalid'}
    urls['long'] = {'url': 'https://www.google.com/1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'error': 'length'}
    urls['valid'] = {'url': 'https://devguide.python.org/documentation/style-guide/#style-guide', 'error': ''}

    return urls


@pytest.fixture()
def check():
    checks = {}
    checks['right'] = 'https://www.facebook.com/'
    checks['wrong'] = 'http://wrong.com'

    return checks


def test_validation_errors(site):
    assert validate_url(site['zero']['url']) == {'url': site['zero']['url'], 'error': 'zero'}
    assert validate_url(site['invalid']['url']) == {'url': site['invalid']['url'], 'error': 'invalid'}
    assert validate_url(site['long']['url']) == {'url': site['long']['url'], 'error': 'length'}

    # valid = 'https://devguide.python.org'
    # assert validate_url(site['valid']['url']) == {'url': valid, 'error': ''}


def test_check(check):
    right = get_url_data(check['right'])
    assert right == {'description': 'Log into Facebook to start sharing and connecting with your friends, family, and people you know.', 'h1': '', 'status_code': 200, 'title': 'Facebook - log in or sign up'}

    with pytest.raises(RequestException):
        get_url_data(check['wrong'])
