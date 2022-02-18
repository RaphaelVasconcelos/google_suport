PYTHON_VERSION = 3.9.5
PYTHON_CURRENT_VERSION = $(shell python --version | cut -d " " -f2)

default: run

ifeq ($(shell which poetry), )
	$(info Please run `make install-deps`)
	$(error )
else
	POETRY_PYTHON_VERSION = $(shell poetry env info | grep Python: | sed -e "s/ //g" | cut -d ":" -f2 | head -n 1)
endif

ifneq ($(PYTHON_CURRENT_VERSION), $(PYTHON_VERSION))
	$(info Require python version $(PYTHON_VERSION))
	$(error )
endif

ifneq ($(POETRY_PYTHON_VERSION), $(PYTHON_VERSION))
	@poetry env use $(PYTHON_VERSION)
endif

init: install-deps

install-deps:
	@pip3 install --upgrade pip setuptools wheel
	@pip3 install --upgrade poetry

poetry-export:
	@poetry export --dev -vv --no-ansi --no-interaction --format requirements.txt --output requirements.txt

lock-deps:
	@poetry lock -vv --no-ansi --no-interaction

add-deps:
ifeq ($(libs), )
	$(info Please run `make add-dev-deps libs="lib1==version ...lib[n]==version"`)
	$(error )
endif
	@poetry add -vv --no-ansi --no-interaction $(libs)

add-dev-deps:
ifeq ($(libs), )
	$(info Please run `make add-dev-deps libs="lib1==version ...lib[n]==version"`)
	$(error )
endif
	@poetry add -vv --no-ansi --no-interaction --dev $(libs)

rm-deps:
ifeq ($(libs), )
	$(info Please run `make rm-deps libs="lib1 ...lib[n]"`)
	$(error )
endif
	@poetry remove -vv --no-ansi --no-interaction $(libs)

run:
	@poetry install
	@poetry run env $(shell cat .env | grep -v ^\# | xargs) poetry run python3 main.py

build-container:
	@docker build \
		--tag pagar.me:risk-actions \
		--build-arg GIT_HASH=$(shell git rev-parse HEAD) \
		.

run-container: poetry-export build-container
	@docker run --rm -it \
		--name pagar.me_risk-actions \
		--env-file .env \
		--env PORT=8080 \
		--publish 8080:8080 \
		pagar.me:risk-actions

test-all:
	@poetry run env $(shell cat .env | grep -v ^\# | xargs) pytest
