PYTHON_BIN :=.venv/bin

all: install

.PHONY: install .venv test serve deploystatic fixtures check-aws-env

install: .venv

.venv: $(PYTHON_BIN)/activate

check-aws-env:
ifndef AWS_ACCESS_KEY
	$(error AWS_ACCESS_KEY is undefined)
endif
ifndef AWS_SECRET_ACCESS_KEY
	$(error AWS_SECRET_ACCESS_KEY is undefined)
endif

$(PYTHON_BIN)/activate: requirements.txt
	test -d $(PYTHON_BIN) || virtualenv .venv
	$(PYTHON_BIN)/pip install -Ur requirements.txt
	touch $(PYTHON_BIN)/activate

fixtures:
	$(PYTHON_BIN)/python manage.py migrate
	$(PYTHON_BIN)/python manage.py populate

test:
	$(PYTHON_BIN)/pytest

serve:
	$(PYTHON_BIN)/python manage.py runserver

deploystatic: check-aws-env
	$(PYTHON_BIN)/python manage.py collectstatic --noinput
