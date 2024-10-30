#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:19:26 2024

@author: marcus
"""

import cpuinfo

def getLocalCPU():
    local_CPU_info = cpuinfo.get_cpu_info()
    return local_CPU_info
# print(localCPUInfo)
# print(type(localCPUInfo))
# print(localCPUInfo['brand_raw'])

cpu_info = getLocalCPU()
ext_CPU_info = cpu_info['brand_raw']
print(ext_CPU_info)

#### 
## Get the IP address


## Get the mac address
import uuid
# from uuid import getnode as get_mac
# mac = get_mac()
# print(mac)

test_MAC = uuid.getnode()
print(test_MAC)
print(type(test_MAC))

mac2 = ':'.join(f"{(test_MAC >> i) & 0xff:02x}" for i in range(0, 48, 8)[::-1])
print(mac2)

mac3 = hex(test_MAC)
print(mac3)
# reduce the complexity
# macstring performs the clearest form of mac address and it is the correct form of valid address
# here the for loop arranges the valid mac address in orderly formats
macString=':'.join(("%012X" % test_MAC) [i:i+2] for i in range(0,12,2))
# now print the valid mac address in the correct format
print("The MAC address is",'[' + macString + ']')

# Another option 
print ("The MAC address in formatted way is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

## A third option 
import re, uuid
# joins elements of getnode() after each 2 digits.
# using regex expression
print ("The MAC address in formatted and less complex way is : ", end="")
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))

import getmac



## IP ADDRESS stuff
## what IP address am I getting the MAC address of
import psutil
for interface in psutil.net_if_addrs():
    # Check if the interface has a valid MAC address
    print(interface)
    if psutil.net_if_addrs()[interface][0].address:
        # Print the MAC address for the interface
        print(psutil.net_if_addrs()[interface][0].address)
        #break

totalPSUTILS = psutil.net_if_addrs()

## print(totalPSUTILS) # not ideal.. has key value pairs



###  lets use socket to do this
import socket

## create a socket using UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

## connect to Google on port 80
s.connect(("8.8.8.8", 80))

# print("I have connected")
# get the list
#print(s.getsockname())

# store it as a variable for later.
socketName = s.getsockname()

# print(s.getsockname()[0])  # get the first item
# don't forget to close the connection

s.close()
print(socketName[0])


### try PSUTILS for ports
port_list = psutil.net_connections()
print(len(port_list))  ## this shows how many items in the list



