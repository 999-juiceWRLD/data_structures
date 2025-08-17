#!/bin/bash

cd "$(dirname "$0")"
source venv/bin/activate

python -m unittest discover -s test -p "test_*.py"