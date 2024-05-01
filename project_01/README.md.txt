Project 1: Pocket Plant

Hackster link: https://www.hackster.io/ameliapillar/pocket-plant-af2e39

Libraries to install:
sudo apt-get update
sudo apt-get install fbi
sudo apt-get install python3.5-dev
sudo apt-get install python3-pip
sudo pip3 install Adafruit-GPIO
sudo pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-bh1750

The "code" folder of this repository contains a folder for the driver of each component, as well as the main code in "main". "main" also contains the run file, which has file paths to the drivers, and a configure pins file, which has the pins for each component. If your file paths change or you use different pins, modify these files.

To run the program:
  - clone the github repository
  - cd /var/lib/cloud9/ENGI301/project_01
  - sudo ./run



Currently, the code is not fully operational, but possible future work would include more indepth debugging to get everything up and running.
