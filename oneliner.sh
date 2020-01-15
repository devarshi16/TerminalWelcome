#!/bin/bash
file="/home/$USER/fortunes.txt"
if [ -f "$file" ]; then
    shuf -n 1 $file
fi
cp ./fortunes.txt $HOME/fortunes.txt
