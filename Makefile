# Configuration
PYTHON_FILES := $(shell find . -name "*.py")

# Default target
all: format lint

# Install all python dependencies
install:
	pipenv install

# Format code using black
format:
	black $(PYTHON_FILES)

# Run pylint
lint:
	pylint --disable=R,C $(PYTHON_FILES)

# Run unit tests
test:
	python -m pytest -vv test_*.py

# Run the server
run:
	uvicorn todo.server:server --reload