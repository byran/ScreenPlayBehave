@echo off

cd "%~dp0"

call .venv\Scripts\activate.bat

coverage run --branch --module pytest --junit-xml=docs/unittest_results/unittest_results.xml
set EXIT_CODE=%ERRORLEVEL%

coverage report --omit=".venv/*" --show-missing

coverage html --omit=".venv/*" -d docs/_static/coverage

exit /B %EXIT_CODE%
