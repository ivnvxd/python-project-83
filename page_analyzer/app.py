from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   flash,
                   get_flashed_messages
                   )
import os
from dotenv import load_dotenv
from datetime import datetime
import requests

from page_analyzer.checks import (validate_url,
                                  get_url_data
                                  )
from page_analyzer.db import (get_all_urls,
                              get_urls_by_id,
                              get_urls_by_name,
                              get_checks_by_id,
                              add_check,
                              add_site)


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


# @app.errorhandler(404)
# def page_not_found():
#     return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template(
        'index.html',
    )


@app.get('/urls')
def urls_get():

    urls = get_all_urls()

    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'urls.html',
        urls=urls,
        messages=messages
    )


@app.post('/urls')
def urls_post():

    url = request.form.get('url')
    check = validate_url(url)

    url = check['url']
    error = check['error']

    if error:
        if error == 'exists':

            id_ = get_urls_by_name(url)[0]['id']

            flash('Страница уже существует', 'alert-info')
            return redirect(url_for(
                'url_show',
                id_=id_
            ))
        else:
            flash('Некорректный URL', 'alert-danger')

            if error == 'zero':
                flash('URL обязателен', 'alert-danger')
            elif error == 'length':
                flash('URL превышает 255 символов', 'alert-danger')

            messages = get_flashed_messages(with_categories=True)
            return render_template(
                'index.html',
                url=url,
                messages=messages
            ), 422

    else:
        site = {
            'url': url,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        add_site(site)

        id_ = get_urls_by_name(url)[0]['id']

        flash('Страница успешно добавлена', 'alert-success')
        return redirect(url_for(
            'url_show',
            id_=id_
        ))


@app.route('/urls/<int:id_>')
def url_show(id_):

    url = get_urls_by_id(id_)[0]
    checks = get_checks_by_id(id_)

    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'show.html',
        url=url,
        checks=checks,
        messages=messages
    )


@app.post('/urls/<int:id_>/checks')
def url_check(id_):

    url = get_urls_by_id(id_)[0]['name']

    try:
        check = get_url_data(url)

        check['url_id'] = id_
        check['checked_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        add_check(check)

        flash('Страница успешно проверена', 'alert-success')
        return redirect(url_for(
            'url_show',
            id_=id_
        ))

    except requests.ConnectionError:
        flash('Произошла ошибка при проверке', 'alert-danger')
        return redirect(url_for(
            'url_show',
            id_=id_
        ))


if __name__ == '__main__':
    app.run()
