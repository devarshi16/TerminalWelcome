#!/bin/bash
echo 'echo "Welcome Devarshi "' >> ~/.bashrc
echo 'echo "|\_                  _ "' >> ~/.bashrc
echo 'echo " \ \               _/_|"' >> ~/.bashrc
echo 'echo "  \ \_          __/ /"' >> ~/.bashrc
echo 'echo "   \  \________/   /"' >> ~/.bashrc
echo 'echo "    |              |"' >> ~/.bashrc
echo 'echo "    /              |"' >> ~/.bashrc
echo 'echo "   |   0       0   |"' >> ~/.bashrc
echo 'echo "   |       _       |"' >> ~/.bashrc
echo 'echo "   |()    __    () |"' >> ~/.bashrc
echo 'echo "    \    (__)      |"' >> ~/.bashrc
echo 'file="/home/$USER/fortunes.txt"' >> ~/.bashrc
echo 'if [ -f "$file" ]' >> ~/.bashrc
echo 'then' >> ~/.bashrc
echo '    shuf -n 1 $file' >> ~/.bashrc
echo 'fi' >> ~/.bashrc
cp ./fortunes.txt /home/$USER/fortunes.txt