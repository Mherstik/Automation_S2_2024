#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:55:09 2024

@author: marcus
"""

#Here's how you can check if a Python module is installed and install it if it is not:

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_install(package):
    try:
        __import__(package)
        print(f"{package} is available")
    except ImportError:
        print(f"{package} not available.\nInstalling now...")
        install(package)

# Example usage:
# check_install("psutil")
# check_install("speedtest-cli")

packageList = ['uuid','psutil', 'speedtest-cli', 'pandas', 'certifi']

# uuid required for mac address
# psutil required for 
# speedtest-cli needs to be imported as just speedtest
# pandas is only required if you use the pandas data frame
#
# certifi is needed for checking the https connection this is new to
###  we will get rid of the check if there is a problem

for package in packageList:
    check_install(package)


from time import time, ctime, gmtime
import os
import sys
import csv
import ssl
## speedtest starts
## 
import urllib.request # to get the url




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
    context = ssl._create_unverified_context()  # Skip SSL verification
    
    start_time = time()  # or time.time()
    #print(start_time)
    ## DO TESTS
    with urllib.request.urlopen(url, context=context) as response:
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
