VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PROJECT_ROOT = src


$(VENV)/bin/activate: requirements/dev.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements/dev.txt


install:
	make $(VENV)/bin/activate

clean:
	rm -rf __pycache__

fmt:
	black ./

lint:
	pylint ${PROJECT_ROOT}/

types:
	mypy ${PROJECT_ROOT}/ --strict

check:
	make fmt
	make lint
	make types


test:
	python -m pytest --cov=src --cov-report=html --cov-fail-under=80 tests/

run:
	python -m src.main
