#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:38:36 2024

@author: marcus
"""

from time import time, ctime, gmtime

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
os_name = os.name
os_uname = os.uname()
print(os.name)
print(os.uname())

import sys
print("Using SYS")
print(sys.platform)
osType = sys.platform
print(sys.version)  # this tells you Python version

print("Using PLATFORM")
import platform
print(platform.system())


## adding random stuff
## 
def get_IPaddress():
    if osType == "linux":
        print(os.system('ip a'))
    else:
        print(os.system('ipconfig'))
# this has issues as it's using the OS commands
get_IPaddress()

### open file to write to it
#  check to see if file exists...?

# open for writing
with open("testfile.csv", 'w') as f:
    f.write(str(pcTime + "," + osType + "," + os_name))

with open('testfile.csv', 'r') as f:
    print(f.read())
    



## stolen from https://www.geeksforgeeks.org/get-your-system-information-using-python-script/
import platform

my_system = platform.uname()

print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")




# import socket
# local_name = socket.gethostname()
# print(local_name)
# # this tries to connect to Google DNS
# # and tells what IP did the connection
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# # get the local IP from the socket connection
# local_ip = s.getsockname()
# print(local_ip)
# # only get the first index from the list
# print("the IP that connected is from",s.getsockname()[0])

