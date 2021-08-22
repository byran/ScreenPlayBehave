#!/usr/bin/env bash

readonly SCRIPT_PATH=$(realpath $(dirname $0))
cd "$SCRIPT_PATH"

source .venv/bin/activate

coverage run --branch --module pytest --junit-xml=docs/unittest_results/unittest_results.xml
readonly EXIT_CODE=$?

coverage report --omit=".venv/*" --show-missing

coverage html --omit=".venv/*" -d docs/_static/coverage

exit ${EXIT_CODE}
