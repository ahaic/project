#!/bin/bash

#===============================================================================================
#   System tested:  raspberry pi
#   Description:  A tool to auto-compile & install python-opencv on Linux
#   Author: ahaic
#   Date: 23 Oct 2019
#===============================================================================================

echo ""
echo "+---------------------------------------------------------+"
echo "|        opencv for Linux Server, Written by ahaic        |"
echo "+---------------------------------------------------------+"
echo "|     A tool to auto-compile & install opencv on Linux    |"
echo "+---------------------------------------------------------+"



echo "installing python-opencv for python3"

sudo apt-get install libatlas-base-dev -y 
sudo apt-get install libjasper-dev -y
sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev -y  
apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y  
sudo apt-get install libqt4-test -y
yes | pip3 install opencv-python -y 
sudo apt-get install libqtgui4 -y


echo 'Current status -------->> finished !'
echo "+---------------------------------------------------------+"
echo "|   test on  python3   import cv2    cv2.__version__      |"
echo "+---------------------------------------------------------+"
