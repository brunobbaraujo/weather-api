.PHONY: all

TEST_PY:=$(wildcard tests/*.py)

SRC_FILES := $(wildcard */*.py)
SRC_FILES := $(filter-out tests/*.py, $(SRC_FILES))

test:  ## Run tests
	pytest -ff -n 4 $(TEST_PY)

fmt: ## fmt files
	isort $(SRC_FILES)
	black $(SRC_FILES)