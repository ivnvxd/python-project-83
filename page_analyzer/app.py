from flask import Flask, \
    render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls')
def urls_get():
    data = {}
    return render_template(
        'urls.html',
        data=data
    )


@app.route('/urls/<int:id>')
def url_show(id):
    return render_template(
        'show.html',
        id=id
    )
