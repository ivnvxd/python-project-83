from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   flash
                   )
import os
from psycopg2 import connect
import psycopg2.extras
from dotenv import load_dotenv
from datetime import datetime

import validators
from urllib.parse import urlparse


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

DATABASE_URL = os.getenv('DATABASE_URL')


# @app.errorhandler(404)
# def page_not_found():
#     return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/urls')
def urls_get():
    conn = connect(DATABASE_URL)
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        q_select = '''SELECT DISTINCT ON (urls.id)           
	                    urls.id AS id,
	                    urls.name AS name,
	                    url_checks.created_at AS last_check,
	                MAX(url_checks.id) AS check_no
                    FROM urls 
                    LEFT JOIN url_checks ON urls.id = url_checks.url_id
                    GROUP BY urls.id, url_checks.created_at
                    ORDER BY urls.id DESC'''
        cur.execute(q_select)
        urls = cur.fetchall()
    conn.close()

    return render_template(
        'urls.html',
        urls=urls
    )


@app.post('/urls')
def urls_post():

    url = request.form.get('url')
    check = validate_url(url)
    url = check['url']
    error = check['error']

    if error:
        if error == 'exists':
            conn = connect(DATABASE_URL)
            with conn.cursor() as cur:
                q_select = 'SELECT id FROM urls WHERE name=(%s)'
                cur.execute(q_select, [url])
                id_ = cur.fetchone()[0]
            conn.close()

            flash('Страница уже существует', 'alert-info')
            return redirect(url_for('url_show', id_=id_))
        else:
            flash('Некорректный URL', 'alert-danger')

            if error == 'zero':
                flash('URL обязателен', 'alert-danger')
            elif error == 'length':
                flash('URL превышает 255 символов', 'alert-danger')

            return render_template('index.html', url=url), 422

    else:
        created_at = datetime.now().date()

        conn = connect(DATABASE_URL)
        with conn.cursor() as cur:
            q_insert = 'INSERT INTO urls (name, created_at) VALUES (%s, %s)'
            cur.execute(q_insert, (url, created_at))

            q_select = 'SELECT id FROM urls WHERE name=(%s)'
            cur.execute(q_select, [url])
            id_ = cur.fetchone()[0]
            conn.commit()
        conn.close()

        flash('Страница успешно добавлена', 'alert-success')
        return redirect(url_for(
            'url_show',
            id_=id_
        ))


@app.route('/urls/<int:id_>')
def url_show(id_):

    conn = connect(DATABASE_URL)
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        q_select = 'SELECT id, name, created_at FROM urls WHERE id=(%s)'
        cur.execute(q_select, [id_])
        url = cur.fetchone()

        q_select = 'SELECT id, created_at FROM url_checks WHERE url_id=(%s) ORDER BY id DESC'
        cur.execute(q_select, [id_])
        checks = cur.fetchall()
    conn.close()

    return render_template(
        'show.html',
        id=id_,
        url=url,
        checks=checks
    )


@app.post('/urls/<int:id_>/checks')
def url_check(id_):
    checked_at = datetime.now().date()
    url_id = id_

    conn = connect(DATABASE_URL)
    with conn.cursor() as cur:
        q_insert = 'INSERT INTO url_checks (url_id, created_at) VALUES (%s, %s)'
        cur.execute(q_insert, (url_id, checked_at))
        conn.commit()
    conn.close()

    flash('Страница успешно проверена', 'alert-success')
    return redirect(url_for(
        'url_show',
        id_=id_
    ))


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

        conn = connect(DATABASE_URL)
        cur = conn.cursor()
        q_select = 'SELECT id, name FROM urls WHERE name=(%s)'
        cur.execute(q_select, [norm_url])

        found = cur.fetchall()

        cur.close()
        conn.close()

        if found:
            error = 'exists'

        url = norm_url

    return {'url': url, 'error': error}


if __name__ == '__main__':
    app.debug = True
    app.run()
