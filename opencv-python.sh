#!/bin/bash

#===============================================================================================
#   System Required:  raspberry pi
#   Description:  A tool to auto-compile & install python-opencv on Linux
#   Author: ahaic
#   Intro:  
#===============================================================================================

echo ""
echo "+---------------------------------------------------------+"
echo "|        frps for Linux Server, Written by Clang           |"
echo "+---------------------------------------------------------+"
echo "|     A tool to auto-compile & install opencv on Linux      |"
echo "+---------------------------------------------------------+"
echo "|    Intro:     |"
echo "+---------------------------------------------------------+"
echo ""


echo "installing python-opencv for python3"

sudo apt-get install libatlas-base-dev -y 1>/dev/null 2>&1
sudo apt-get install libjasper-dev -y 1>/dev/null 2>&1
sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev -y  1>/dev/null 2>&1
apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y  1>/dev/null 2>&1
sudo apt-get install libqt4-test -y 1>/dev/null 2>&1
pip3 install opencv-python -y 1>/dev/null 2>&1



echo 'Current status -------->> finished !'
