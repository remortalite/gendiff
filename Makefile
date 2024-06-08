install:
	poetry install

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

show-coverage:
	poetry run pytest --cov=gendiff --cov-report term-missing

test:
	poetry run pytest
