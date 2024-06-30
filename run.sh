#!/bin/bash
PARAMS="${*:2}"

case $1 in
    tests)
    echo "Tests...."

    if [[ -z "${PARAMS}" ]]; then
        PARAMS="tests"
    fi

    # run tests
    pytest "${PARAMS}"
    ;;

    coverage)
    echo "Running...."

    if [[ -z "${PARAMS}" ]]; then
        PARAMS="coverage"
    fi

    coverage run "${PARAMS}"

    ;;

    server)

    python manage.py runserver

    ;;

    shell)

    ipython

    ;;

    *)
        echo "Option not found, use one of these: coverage, tests"
        exit 1
    ;;

esac


# ./run.sh server