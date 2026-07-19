#!/bin/bash
PARAMS="${*:2}"

# Use the local virtualenv without needing it activated in the shell first.
VENV="$(dirname "$0")/.venv"
if [[ -d ${VENV} ]]; then
    PATH="${VENV}/bin:${PATH}"
    export PATH
fi


if [[ -z ${PARAMS} ]]; then
    TESTS='tests.py'
else
    TESTS="${PARAMS}"
fi


case $1 in
    tests)

    # run tests
    python -m pytest "${TESTS}"
    ;;

    coverage)
    echo "Running...."

    coverage run "${TESTS}"
    coverage report 
    ;;

    server)

    FLASK_APP=app flask run --debug --port "${PORT:-8000}"

    ;;

    shell)

    ipython3

    ;;

    prod-server)

    gunicorn app:app --bind "0.0.0.0:${PORT:-8000}"

    ;;

    virtual-env)

    # Activation only sticks if this script was sourced, since a subshell
    # throws the change away on exit. Run it as: source run.sh virtual-env
    if [[ ${BASH_SOURCE[0]} == "$0" ]]; then
        echo "This command must be sourced, otherwise the activation is lost:"
        echo "    source run.sh virtual-env"
        exit 1
    fi

    if [[ ! -d ${VENV} ]]; then
        echo "No virtualenv at ${VENV}. Create it with:"
        echo "    python3 -m venv .venv && ./run.sh install"
        return 1
    fi

    . "${VENV}/bin/activate"
    echo "Virtualenv activated: ${VIRTUAL_ENV}"

    ;;

    install)

    python -m pip install -r requirements.txt

    ;;

    *)
        echo "Option not found, use one of these: coverage, tests, shell, server, prod-server, install, virtual-env"
        exit 1
    ;;
esac