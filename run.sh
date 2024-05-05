#!/bin/bash
PARAMS="${*:2}"

case $1 in
    tests)

    if [[ -z "${PARAMS}" ]]; then
        PARAMS="tests"
    fi

    # run tests
    pytest "${PARAMS}"
    ;;

    *)
        echo "Option not found, use one of these: coverage, tests"
        exit 1
    ;;

esac