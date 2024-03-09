local:
	python main.py

test:
	pytest -v

check-coverage:
	coverage run --source=./ -m pytest -v && coverage report