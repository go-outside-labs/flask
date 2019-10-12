.DELETE_ON_ERROR:

venv:
	virtualenv venv

install:
	pip install -r requirements.txt

clean:
	rm -rf '*.pyc' '*.pyo' build/ .tox/ dist/ *.egg-info __pycache__ *db

run:
	python ./src/app.py

test:
	pytest

.PHONY: all venv install clean test
