#!/usr/bin/env bash

python3 -m pip install poetry
poetry config virtualenvs.path false
poetry install