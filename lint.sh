#!/bin/bash

set -e

. .venv/bin/activate

echo Checking for syntax errors
flake8 . --exclude=.venv --count --select=E9,F63,F7,F82 --show-source --statistics

echo Linting
flake8 . --exclude=.venv --count --max-complexity=10 --max-line-length=127 --statistics --ignore=F811
