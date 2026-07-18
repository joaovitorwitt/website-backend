#!/bin/bash
PARAMS="${*:2}"


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

    . .venv/bin/activate

    ;;

    *)
        echo "Option not found, use one of these: coverage, tests, shell, server"
        exit 1
    ;;
esac


# run sh to activate virtual environment