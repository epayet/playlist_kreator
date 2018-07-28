compile-requirements:
	pip-compile  --no-index -o requirements.txt requirements.in constraints.txt
	@sed -i.bak 's/#    pip-compile.*/#    make compile-requirements/g' requirements.txt
	@rm -f requirements.txt.bak