
install:
	pip install --upgrade pip && pip install -r Requirements.txt

format:
	black *.py

lint:
	ruff check *.py test_*.py 
# mylib/*.py *.ipynb	
test: 
	python -m pytest -cov=main test_main.py

all: install format lint test 




