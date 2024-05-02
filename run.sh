#!/bin/bash

# Check if the argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <command>"
    exit 1
fi

# Check if the provided argument is 'tests'
if [ "$1" = "tests" ]; then
    # Run pytest with the 'tests' argument
    pytest tests
else
    echo "Invalid command. Usage: $0 <command>"
    exit 1
fi