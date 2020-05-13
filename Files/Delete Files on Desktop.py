#! /usr/bin/env python3

import os

os.chdir(os.path.expanduser("~")) #adapted for windows, mac and linux users
desktopPath = os.path.abspath('desktop')
os.chdir(desktopPath)
for filename in os.listdir():
    os.unlink(filename)
