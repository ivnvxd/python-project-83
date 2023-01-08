import validators
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

from page_analyzer.db import get_urls_by_name


def validate_url(url):
    error = None

    if len(url) == 0:
        error = 'zero'
    elif len(url) > 255:
        error = 'length'
    elif not validators.url(url):
        error = 'invalid'
    else:
        parsed_url = urlparse(url)
        norm_url = f'{parsed_url.scheme}://{parsed_url.netloc}'

        found = get_urls_by_name(norm_url)

        if found:
            error = 'exists'

        url = norm_url

    valid = {'url': url, 'error': error}

    return valid


def get_url_data(url: str) -> dict:
    check = {}

    r = requests.get(url)
    check['status_code'] = r.status_code

    soup = BeautifulSoup(r.text, 'html.parser')

    h1_tag = soup.find('h1')
    title_tag = soup.find('title')
    description_tag = soup.find('meta', attrs={'name': 'description'})

    check['h1'] = h1_tag.text.strip() if h1_tag else ''
    check['title'] = title_tag.text.strip() if title_tag else ''
    check['description'] = description_tag['content'].strip() \
        if description_tag else ''

    return check
