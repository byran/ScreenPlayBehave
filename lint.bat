@echo off

cd "%~dp0"

call .venv\Scripts\activate.bat

echo Checking for syntax errors
flake8 . --exclude=.venv --count --select=E9,F63,F7,F82 --show-source --statistics

echo Linting
flake8 . --exclude=.venv --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --ignore=F811
