.PHONY: clean
clean:
	@find . -iname '*.py[co]' -delete
	@find . -iname '__pycache__' -delete
	@rm -rf  '.pytest_cache'
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info
	@rm -rf .tox
	@rm -rf venv/
	

.PHONY: build
build:
	@PYTHONPATH=$(pwd) virtualenv venv
	@PYTHONPATH=$(pwd) source venv/bin/activate
	@PYTHONPATH=$(pwd) pipenv install
	@PYTHONPATH=$(pwd) pipenv shell

.PHONY: install
install:
	@PYTHONPATH=$(pwd) python3 setup.py install

.PHONY: lint
lint:
	@PYTHONPATH=$(pwd) tox -e lint

.PHONY: test
test:
	@PYTHONPATH=$(pwd) tox

.PHONY: api
api:
	@PYTHONPATH=$(pwd) python3 run_local.py