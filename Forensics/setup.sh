#!/bin/bash
sudo apt-get upgrade
sudo apt-get install volatility
sudo apt-get install foremost
wget https://github.com/devttys0/binwalk/archive/master.zip
sudo apt install unzip
unzip master.zip
chmod +x ./binwalk-master/deps.sh
sudo ./binwalk-master/deps.sh
