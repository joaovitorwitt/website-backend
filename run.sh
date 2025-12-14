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

    flask run

    ;;

    shell)

    ipython3

    ;;

    prod-server)

    hypercorn app:asgi_app

    ;;

    *)
        echo "Option not found, use one of these: coverage, tests, shell, server"
        exit 1
    ;;
esac
