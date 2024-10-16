#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:15:11 2024

@author: marcus
"""
from time import time, ctime, gmtime

def get_time():
    t = time()
    return (ctime(t)) #, gmtime(t))

pcTime = get_time()

import os
os_name = os.name


import sys
osType = sys.platform

### open file to write to it
#  check to see if file exists...?

# open for writing
with open("testfile.csv", 'w') as f:
    f.write(str(pcTime + "," + osType + "," + os_name))

with open('testfile.csv', 'r') as f:
    print(f.read())
    
