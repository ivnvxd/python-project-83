from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for
                   )
import os
from psycopg2 import connect
import psycopg2.extras
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import urlparse


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

DATABASE_URL = os.getenv('DATABASE_URL')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls', methods=['GET', 'POST'])
def urls_get():

    if request.method == 'POST':
        url = request.form.get('url')
        parsed_url = urlparse(url)
        norm_url = f'{parsed_url.scheme}://{parsed_url.netloc}'

        date = datetime.now().date()

        conn = connect(DATABASE_URL)
        cur = conn.cursor()

        q_insert = 'INSERT INTO urls (name, created_at) VALUES (%s, %s)'
        cur.execute(q_insert, (norm_url, date))

        q_select = 'SELECT id FROM urls WHERE name=(%s)'
        cur.execute(q_select, [norm_url])
        id = cur.fetchone()[0]

        conn.commit()

        cur.close()
        conn.close()

        return redirect(url_for(
            'url_show',
            id=id
        ))

    else:
        conn = connect(DATABASE_URL)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        q_select = 'SELECT id, name, created_at FROM urls ORDER BY id DESC;'
        cur.execute(q_select)

        urls = cur.fetchall()

    cur.close()
    conn.close()

    # return DATABASE_URL

    return render_template(
        'urls.html',
        urls=urls
    )


@app.route('/urls/<int:id>')
def url_show(id):

    conn = connect(DATABASE_URL)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    q_select = 'SELECT id, name, created_at FROM urls WHERE id=(%s)'
    cur.execute(q_select, [id])
    url = cur.fetchone()
    cur.close()
    conn.close()

    return render_template(
        'show.html',
        id=id,
        url=url
    )
