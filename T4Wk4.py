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

url = 'https://github.com/Mherstik/Automation_S2_2024/raw/refs/heads/main/20MB.zip'
# url = 'http://speed.hetzner.de/100MB.bin'


def checkSpeed(url):
    '''

    Parameters
    ----------
    url : a GitHub URL
        This will be a file on GitHub

    Returns
    -------
    speed : float
        the speed divided by the time it took to download.

    '''
    start_time = time()  # or time.time()
    #print(start_time)
    ## DO TESTS
    with urllib.request.urlopen(url) as response:
        response.read()
    stop_time = time()
    #print(stop_time)
    downloadTime = stop_time - start_time
    print(f'Elapsed time is {stop_time - start_time}')
    speed = (20 * 8) / downloadTime
    #print(f'Speed is {speed} from inside the checkSpeed')
    return speed

speed = checkSpeed(url)
print(f'Download speed was {speed:.2f} Mbps')

help(checkSpeed)
### OPTIONAL WITH SPEEDTEST-CLI module
### 
import speedtest
servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
download_speed = s.download(threads=threads)
upload_speed = s.upload(threads=threads)
print(download_speed /1024/1024, upload_speed/1024/1024)
s.results.share()

results_dict = s.results.dict()
dl = results_dict.get('download')
print(dl/1024/1024)



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