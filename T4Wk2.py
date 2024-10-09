#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:38:36 2024

@author: marcus
"""

from time import time, ctime, gmtime

pcTime = ''

def get_time():
    t = time()
    return (ctime(t)) #, gmtime(t))

pcTime = get_time()
print(pcTime)

from datetime import datetime #, timezone
def get_Datetime():
    return datetime.now()

secondTime = get_Datetime()
print(secondTime)
# print(datetime.utcnow())
# print(timezone)


import os
print("Using OS")
print(os.name)
print(os.uname())

import sys
print("Using SYS")
print(sys.platform)
print(sys.version)  # this tells you Python version

print("Using PLATFORM")
import platform
print(platform.system())
