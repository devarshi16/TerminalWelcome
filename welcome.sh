#!/bin/bash
file="$HOME/fortunes.txt"
if [ ! -f "$file" ]; then
    cp "$(dirname "$0")/fortunes.txt" "$file"
fi

cat <<'EOF' >> "$HOME/.bashrc"
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
file="$HOME/fortunes.txt"
if [ -f "$file" ]; then
    shuf -n 1 "$file"
fi
EOF

