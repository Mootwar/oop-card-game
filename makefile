# Variables
PYTHON := python3
FLAKE8 := flake8
PYTEST := pytest
COV_REPORT_DIR := report
MAIN_SCRIPT := main.py

# Default target
all: lint test_coverage

# Linting with flake8
lint:
	@echo "Running flake8 linting..."
	$(FLAKE8) . --count --select=E9,F63,F7,F82 --show-source --statistics
	$(FLAKE8) . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

# Run tests as a module with coverage and generate HTML and terminal reports
test_coverage:
	@echo "Running tests in /test/tests.py as a module and generating coverage reports..."
	$(PYTHON) -m pytest test/tests.py --cov=classes --cov-report=term --cov-report=html:$(COV_REPORT_DIR)

# Run the main script
play:
	@echo "Running main.py..."
	$(PYTHON) $(MAIN_SCRIPT)

# Clean up generated files
clean:
	@echo "Cleaning up generated files..."
	rm -rf $(COV_REPORT_DIR) .pytest_cache .coverage

# Help
help:
	@echo "Usage:"
	@echo "  make lint           - Run flake8 linting"
	@echo "  make test_coverage  - Run /test/tests.py with coverage and generate HTML and terminal reports"
	@echo "  make run            - Run main.py"
	@echo "  make clean          - Clean up generated files"
	@echo "  make all            - Run both linting and test coverage"
