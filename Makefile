dev:
	poetry run flask --app page_analyzer:app run

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

lint:
	poetry run flake8 page_analyzer

test:
	poetry run pytest --cov=page_analyzer

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

install:
	poetry install

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

package-install:
	pip install --user --force-reinstall dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

# publish:
# 	poetry publish --dry-run
