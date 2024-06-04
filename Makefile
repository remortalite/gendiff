install:
	poetry install

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml


test:
	poetry run pytest
