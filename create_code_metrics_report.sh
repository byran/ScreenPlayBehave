#!/usr/bin/env bash

readonly SCRIPT_PATH=$(realpath $(dirname $0))
cd "$SCRIPT_PATH"

source .venv/bin/activate

radon mi --json > docs_scripts/mi.json .
radon cc --json > docs_scripts/cc.json .
radon raw --json > docs_scripts/raw.json .

cd "$SCRIPT_PATH/docs_scripts"

./create_sourcecode_metrics_sphinx_page.py "$SCRIPT_PATH/docs/metrics/code_metrics.rst"
