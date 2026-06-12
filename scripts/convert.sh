#!/bin/sh
# npm `convert` entry point: prefer the project venv (local dev),
# fall back to system python3 (CI installs nbconvert globally).
set -e
cd "$(dirname "$0")/.."
PY=python3
[ -x .venv/bin/python ] && PY=.venv/bin/python
exec "$PY" scripts/convert_notebooks.py "$@"
