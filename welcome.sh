#!/bin/bash
cat <<EOF >> "$HOME/.bashrc"
echo "Welcome Devarshi "
echo "|\_                  _ "
echo " \ \               _/_|"
echo "  \ \_          __/ /"
echo "   \  \________/   /"
echo "    |              |"
echo "    /              |"
echo "   |   0       0   |"
echo "   |       _       |"
echo "   |()    __    () |"
echo "    \    (__)      |"
file="/home/$USER/fortunes.txt"
if [ -f "$file" ]; then
    shuf -n 1 $file
fi
EOF
cp ./fortunes.txt $HOME/fortunes.txt
