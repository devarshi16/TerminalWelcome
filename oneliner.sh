#!/bin/bash
file="$HOME/fortunes.txt"
if [ ! -f "$file" ]; then
    cp "$(dirname "$0")/fortunes.txt" "$file"
fi
shuf -n 1 "$file"

