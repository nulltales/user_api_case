PYTHON_BIN :=.venv/bin

all: install

.PHONY: install .venv test serve

install: .venv

.venv: $(PYTHON_BIN)/activate

$(PYTHON_BIN)/activate: requirements.txt
	test -d $(PYTHON_BIN) || virtualenv .venv
	$(PYTHON_BIN)/pip install -Ur requirements.txt
	touch $(PYTHON_BIN)/activate

test:
	$(PYTHON_BIN)/pytest

serve:
	$(PYTHON_BIN)/python manage.py runserver
