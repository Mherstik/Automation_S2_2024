#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:24:14 2024

@author: marcus
"""

############
##
##  Some preliminary chat
##
############

from time import time, ctime, gmtime
import os
import sys
import csv
## speedtest
## 
import urllib.request

url = 'http://ipv4.download.thinkbroadband.com/20MB.zip'

def checkSpeed(url):
    pass


speed = checkSpeed(url)
print(f'Download speed was {speed} Mbps')

# Check for modules
# if module not found
#  - install module

# run hostname module
# check if PC has been seen
#   if seen before
#    - ask if they want to overwrite

# run modules

# put all info into file



# ---- 
# Tests

# Against new Windows PC
# Against new Windows PC without file
# Against new Windows PC without modules
# Against new Windows PC without internet
# Against new Windows PC without file and without modules
# Against new Windows PC without file and without modules without internet
# Against duplicate Windows PC 
# Against duplicate Windows PC without file
# Against duplicate Windows PC without internet
#### Against duplicate Windows PC without modules
# Against duplicate Windows PC without file and without modules

# Against new Linux PC
# Against new Linux PC without file
# Against new Linux PC without internet
# Against new Linux PC without modules
# Against new Linux PC without file and without modules
# Against new Linux PC without file and without modules without internet
# Against duplicate Linux PC 
# Against duplicate Linux PC without file
# Against duplicate Linux PC without internet
# Against duplicate Linux PC without modules
# Against duplicate Linux PC without file and without modules
# Against duplicate Linux PC without file and without modules without internet



# # Speedtest CLI
# import sys
# import subprocess
# import pkg_resources

# required = {'speedtest-cli', 'psutil', 'keyboard', 'pyautogui'}
# #required = {'psutil'}
# installed = {pkg.key for pkg in pkg_resources.working_set}

# print(required)
# print(installed)
# missing = required - installed

# if len(missing) > 0:
#     print(f"{missing} is missing")
    
# # print(missing)
# if missing:
#     python = sys.executable
#     subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)    

# input()

# # Check for modules
# import psutil
# import speedtest
# #import pillow

# def speedTestModule():
#     pass

# if module not found
#  - install module

# run hostname module
# check if PC has been seen
#   if seen before
#    - ask if they want to overwrite

# run modules

# put all info into file