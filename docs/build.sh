#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
python -m sphinx -W --keep-going -b html source build/html
