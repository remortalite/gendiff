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

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff


.PHONY: install lint test publish gendiff