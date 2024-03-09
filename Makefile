SHELL := /bin/bash

install-python:
	pyenv install | cat .python-version
	pyenv local | cat .python-version

install-deps:
	pip install -r requirements.txt

create-venv:
	python -m venv .venv

install:
	make install-python
	make create-venv

update-deps:
	pip freeze > requirements.txt

local:
	python main.py

test:
	pytest -v

check-coverage:
	coverage run --source=./ -m pytest -v && coverage report