#!/bin/bash

set -e

port="9000"

. ./venv/bin/activate 
FLASK_APP="api.py" flask run --port="${port}" $@