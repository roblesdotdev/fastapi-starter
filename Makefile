# Configuration
PYTHON_FILES := $(shell find . -name "*.py")

# Default target
all: format lint

# Format code using black
format:
	black $(PYTHON_FILES)

# Run pylint
lint:
	pylint --disable=R,C $(PYTHON_FILES)

# Run unit tests
test:
	python -m pytest -vv test_*.py