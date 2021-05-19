#!/bin/bash
cd "$(dirname "$0")"

python setup.py sdist bdist_wheel
twine upload ./dist/*
