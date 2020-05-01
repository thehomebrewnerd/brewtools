.PHONY: installdeps
installdeps:
	pip install --upgrade pip
	pip install -e .
	pip install -r dev-requirements.txt

.PHONY: lint
lint:
	flake8 brewtools && isort --check-only --recursive brewtools

.PHONY: test
test: lint
	pytest brewtools/

.PHONY: testcoverage
testcoverage:
	pytest brewtools/ --cov=brewtools --cov-report term-missing
