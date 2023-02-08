<div align="center">

<img src="https://raw.githubusercontent.com/ivnvxd/ivnvxd/master/img/h_page_analyzer.png" alt="logo" width="270" height="auto" />
<h1>Page Analyzer</h1>

<p>
Analyze specified pages for SEO suitability
</p>

[![Actions Status](https://github.com/ivnvxd/python-project-83/workflows/hexlet-check/badge.svg)](https://github.com/ivnvxd/python-project-83/actions)
![Run Tests](https://github.com/ivnvxd/python-project-83/actions/workflows/run_tests.yml/badge.svg)
![Lint Check](https://github.com/ivnvxd/python-project-83/actions/workflows/lint_check.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/686717d58de394e8ac7c/maintainability)](https://codeclimate.com/github/ivnvxd/python-project-83/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/686717d58de394e8ac7c/test_coverage)](https://codeclimate.com/github/ivnvxd/python-project-83/test_coverage)

<p>
<a href="#about">About</a> •
<a href="#installation">Installation</a> •
<a href="#usage">Usage</a> •
<a href="#demo">Demo</a> •
<a href="#additionally">Additionally</a> 
</p>
</div>

<details><summary style="font-size:larger;"><b>Table of Contents</b></summary>

* [About](#about)
  * [Features](#features)
  * [Built With](#built-with)
* [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Application](#application)
* [Usage](#usage)
* [Demo](#demo)
* [Additionally](#additionally)
  * [Dependencies](#dependencies)
  * [Dev Dependencies](#dev-dependencies)
  * [Makefile Commands](#makefile-commands)
  * [Project Tree](#project-tree)

</details>

## About

Page Analyzer is a full-featured application based on the Flask framework that analyzes specified pages for SEO suitability. 

Here the basic principles of building modern websites on the MVC architecture are used: working with routing, query handlers and templating, interaction with the database.

In this project the Bootstrap 5 framework along with Jinja2 template engine are used. The frontend is rendered on the backend. This means that the page is built by the Jinja2 backend, which returns prepared HTML. And this HTML is rendered by the server.

PostgreSQL is used as the object-relational database system with Psycopg library to work with PostgreSQL directly from Python.

[Demo](https://python-page-analyzer.up.railway.app/)

### Features

* [X] Validate, normalize and add new URL to the database;
* [X] Check the site for its availability;
* [X] Query the desired site, collect information about it and add it to the database;
* [X] Display all added URLs;
* [X] Display the specific entered URL on a separate page with obtained information;

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Bootstrap 5](https://getbootstrap.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
* [Jinja 2](https://palletsprojects.com/p/jinja/)
* [Psycopg 2](https://www.psycopg.org/)
* [Gunicorn](https://gunicorn.org/)
* [Poetry](https://python-poetry.org/)
* [pytest](https://docs.pytest.org/en/7.2.x/)
* [Flake8](https://flake8.pycqa.org/en/latest/)

---

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8 or higher installed:

```bash
>> python --version
Python 3.8+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

#### PostgreSQL

As database the PostgreSQL database system is being used. You need to install it first. You can download the ready-to-use package from [official website](https://www.postgresql.org/download/) or use Homebrew:
```shell
>> brew install postgresql
```

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/ivnvxd/python-project-83.git && cd python-project-83
```

Then you have to install all necessary dependencies:

```bash
>> make install
```

Create .env file in the root folder and add following variables:
```
DATABASE_URL = postgresql://{provider}://{user}:{password}@{host}:{port}/{db}
SECRET_KEY = '{your secret key}'
```
Run commands from `database.sql` to create the required tables.

---

## Usage

Start the gunicorn Flask server by running:
```bash
make start
```
By default, the server will be available at http://0.0.0.0:8000. 

_It is also possible to start it local in development mode with debugger active using:_
```bash
make dev
```
_The dev server will be at http://127.0.0.1:5000._


To add a new site, enter its address into the form on the home page. The specified address will be validated and then added to the database.

After the site is added, you can start checking it. A button appears on the page of a particular site, and clicking on it creates an entry in the validation table.

You can see all added URLs on the `/urls` page.

---

## Demo

The demo version is available on Railway platform:
[https://python-page-analyzer.up.railway.app/](https://python-page-analyzer.up.railway.app/)

<img src="https://raw.githubusercontent.com/ivnvxd/ivnvxd/master/img/page_analyzer_demo.gif" alt="demo" height="auto" />

---

## Additionally

### Dependencies

* python = "^3.8.1"
* Flask = "^2.2.2"
* gunicorn = "^20.1.0"
* python-dotenv = "^0.21.0"
* psycopg2-binary = "^2.9.5"
* validators = "^0.20.0"
* requests = "^2.28.1"
* beautifulsoup4 = "^4.11.1"

### Dev Dependencies

* flake8 = "^6.0.0"
* pytest = "^7.2.0"
* pytest-cov = "^4.0.0"

### Makefile Commands

<dl>
    <dt><code>make dev</code></dt>
    <dd>Run Flask server in development mode with debugger active.</dd>    
    <dt><code>make start</code></dt>
    <dd>Starts the web server at http://localhost:8000 if no port is specified in the environment variables.</dd>
    <dt><code>make install</code></dt>
    <dd>Install all dependencies of the package.</dd>
    <dt><code>make lint</code></dt>
    <dd>Check code with flake8 linter.</dd>
    <dt><code>make test</code></dt>
    <dd>Run tests.</dd>
    <dt><code>make check</code></dt>
    <dd>Validate structure of <code>pyproject.toml</code> file, check code with tests and linter.</dd>
</dl>

---

<a name="project-tree"></a>
<details><summary style="font-size:larger;"><b>Project Tree</b></summary>

```bash
.
├── Makefile
├── README.md
├── database.sql
├── page_analyzer
│   ├── __init__.py
│   ├── app.py
│   ├── checks.py
│   ├── db.py
│   └── templates
│       ├── 404.html
│       ├── index.html
│       ├── layout.html
│       ├── show.html
│       └── urls.html
├── poetry.lock
├── pyproject.toml
├── setup.cfg
└── tests
    ├── __init__.py
    ├── test_app.py
    └── test_checks.py
```

</details>

---

:octocat: This is the third training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)

> GitHub [@ivnvxd](https://github.com/ivnvxd) &nbsp;&middot;&nbsp;
> LinkedIn [@Andrey Ivanov](https://www.linkedin.com/in/abivanov/)
