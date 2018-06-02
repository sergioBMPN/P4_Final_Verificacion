bootstrap: venv
	venv/bin/pip install -e .
ifneq ($(wildcard requirements.txt),)
	venv/bin/pip install -r requirements.txt
endif

venv:
	virtualenv -p python3 venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
