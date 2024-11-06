#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:27:29 2024

@author: marcus
"""
import time
from urllib import request
import uuid
import re
import os
import csv
import platform

my_system = platform.uname()
nodeName = my_system.node


## FILE READER
### NICER OPENING
def readCSVFile():
    with open(filename, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)

# joins elements of getnode() after each 2 digits.
# using regex expression
mac_add =  ':'.join(re.findall('..', '%012x' % uuid.getnode()))


## Create a Speedtester
def speedtester():
   
    ## start a timer / get current time
    dl_start = time.time()
    #print(dl_start)
    
    ### Download a file
    dl_file = "https://github.com/Mherstik/Automation_Trainee_Nov2024/raw/refs/heads/main/20MB.zip"
    
    ## download the file
    ## using a WITH to have it not stored permanently.
    with request.urlopen(dl_file) as response:
        response.read()
    
    ## stop the timer
    dl_stop = time.time() # dt.datetime.now(tz=None)
    #print(dl_stop)
    
    # Calculate time to download.
    dl_delta = dl_stop - dl_start
    #print(dl_delta)
    
    ## Convert the time to Mbps
    # speed = filesize / downloadtime
    speed = (20 * 8 ) / dl_delta
    return speed

speed = speedtester()
# print(f"Your internet is running at {speed:.2f}Mbps")


## Working with the file
### check if file exists.
## if file DOES NOT exist... write the headers
## if file exists... move to adding speed etc to file
## else add speed etc to file


filename = "aaatester.csv"

isFile = os.path.isfile(filename)

print("---------\nPre writing read!!\n")
# readCSVFile()

## find mac addresses
if isFile == True:
    with open(filename, mode='r') as file:
        csvFile = csv.reader(file)
        i = 1
        for row in csvFile:
            # print(f"checking row {i}")
            macCheck = row[2]
            nodes = row[3]
            # print(macCheck)
            if macCheck == mac_add and nodeName == nodes:
                print(f"Row {i} has a {macCheck} & {nodeName} is a match!")
            # else:
            #     print("no match")
            i = i + 1

f = open(filename, "a")

if isFile == False:
    f.write("Time/Date" + "," + "Speed" + "," + "MAC address" +"," + "Node Name\n")  ## make this optional

f.write(f"{time.ctime()},")
f.write(str(speed) + "," + mac_add + "," + nodeName + "\n")
f.close()

### Read the file
# with open(filename, "r") as f:
#     print(f.read())

# print("read as CSV file\n")
# exampleFile = open('filename')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)


print("\n\n---------\nPost writing read!!\n---------\n\n")

# readCSVFile with Pandas
import pandas as pd
df = pd.read_csv(filename)   # a data frame of the whole file
column_names = list(df.columns)
print(column_names)
colCheck = ['MAC address', 'Node Name']
df2 = pd.read_csv(filename, usecols = colCheck)
print(df2)
###


