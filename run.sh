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
    pytest "${TESTS}"
    ;;

    coverage)
    echo "Running...."

    if [[ -z "${PARAMS}" ]]; then
        PARAMS="coverage"
    fi

    coverage run "${PARAMS}"

    ;;

    server)

    flask run

    ;;

    shell)

    ipython

    ;;

    prod-server)

    hypercorn app:asgi_app

    ;;

    *)
        echo "Option not found, use one of these: coverage, tests, shell, server"
        exit 1
    ;;
esac
