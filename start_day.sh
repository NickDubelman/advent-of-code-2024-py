#!/usr/bin/env bash

# Exit if any command fails
set -e

# Check if the user provided an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <N>"
    exit 1
fi

N="$1"
DIR="day${N}"

# Fail if the directory already exists
if [ -d "$DIR" ]; then
    echo "Error: $DIR already exists."
    exit 1
fi

# Create the directory
mkdir -p "$DIR"

# Create the files inside it
touch "$DIR/part1.py" "$DIR/part2.py" "$DIR/example-input.txt" "$DIR/input.txt"

echo "Created $DIR with part1.py, part2.py, example-input.txt, and input.txt"