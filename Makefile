.PHONY: build test

build:
	pip install -r requirements.txt
	pip install -r build-requirements.txt

test: unit-test integration-test

unit-test:
	pytest tests/unit

integration-test:
	pytest tests/integration

lint:
	python -m flake8

compile-requirements:
	pip-compile  --no-index -o requirements.txt requirements.in constraints.txt
	@sed -i.bak 's/#    pip-compile.*/#    make compile-requirements/g' requirements.txt
	@rm -f requirements.txt.bak

compile-build-requirements:
	pip-compile  --no-index -o build-requirements.txt build-requirements.in
	@sed -i.bak 's/#    pip-compile.*/#    make compile-build-requirements/g' build-requirements.txt
	@rm -f build-requirements.txt.bak

publish:
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload dist/*