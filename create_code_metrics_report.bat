@echo off

cd "%~dp0"

call .venv\Scripts\activate.bat

radon mi --json > docs_scripts/mi.json .
radon cc --json > docs_scripts/cc.json .
radon raw --json > docs_scripts/raw.json .

cd "%~dp0/docs_scripts"

python create_sourcecode_metrics_sphinx_page.py "%~dp0/docs/metrics/code_metrics.rst"

cd "%~dp0"
