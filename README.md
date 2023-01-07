<div align="center">

[//]: # (<img src="" alt="logo" width="300" height="auto" />)
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
  * [Package](#package)
* [Usage](#usage)
* [Demo](#demo)
  *
* [Additionally](#additionally)
  * [Dependencies](#dependencies)
  * [Dev Dependencies](#dev-dependencies)
  * [Makefile Commands](#makefile-commands)
  * [Project Tree](#project-tree)

</details>

## About

Page Analyzer is a full-featured application based on the Flask framework that analyzes specified pages for SEO suitability.

### Features:

* [X] 
* [X] 
* [X] 

### Built With

* Python
* Flask
* Bootstrap 5
* PostgreSQL


* Beautiful Soup 4
* Jinja 2
* Psycopg 2
* gunicorn
* Poetry
* Pytest
* flake8

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

### Package

To use the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project:

```bash
>> git clone https://github.com/ivnvxd/python-project-83.git
```

Then you have to build the package and install it:

```bash
>> cd python-project-83
```


---

## Usage

---

## Demo

[Demo](https://python-project-83-production-c5d0.up.railway.app/)


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
    ├── __pycache__
    └── test_app.py
```

</details>

---

:octocat: This is the third training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)

> GitHub [@ivnvxd](https://github.com/ivnvxd) &nbsp;&middot;&nbsp;
> LinkedIn [@Andrey Ivanov](https://www.linkedin.com/in/abivanov/)
