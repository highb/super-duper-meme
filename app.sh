#!/bin/bash

set -e

component="${1}"
if [ -z "${component}" ]; then
  echo "A component must be provided."
  exit 1
fi
action="${2}"
if [ -z "${action}" ]; then
  echo "A action must be provided. Valid actions: deps, run"
  exit 1
fi

if [ "${action}" == "deps" ]; then
  python3 -m venv "${component}"/venv
fi
. "${component}"/venv/bin/activate 

if [ "${action}" == "deps" ]; then
  pip install -r "${component}"/requirements.txt
fi

if [ "${action}" == "run" ]; then
  if [ "${component}" == "frontend" ]; then
    port="9000"
  elif [ "${component}" == "api" ]; then
    port="9001"
  fi

  FLASK_APP="${component}/${component}.py" flask run --port="${port}"
fi