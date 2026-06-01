PYTHON	=	python3
PIP	=	pip3

.PHONY:	format lint clean

format:
	black .

lint:
	black --check .

clean:
	@echo "Cleaning up..."
	# Remove Python file artifacts
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	# Remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	# Remove test/coverage reports
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/