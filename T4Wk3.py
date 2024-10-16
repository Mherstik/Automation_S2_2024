#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:15:11 2024

@author: marcus
"""
from time import time, ctime, gmtime
import os
import sys

# Get time
def get_time():
    t = time()
    return (ctime(t)) #, gmtime(t))

pcTime = get_time()

# Get OS name
os_name = os.name

# Get OS type
osType = sys.platform

#  check to see if file exists...?
fileName = "testfile.csv"
isExists = os.path.exists(fileName)
print(isExists)

if isExists == True:
    pass
    # do something
else:
    pass
    # do something else
    
# Time, ostype, osname

data = [str(pcTime + "," + osType + "," + os_name)]
print(data)

## pause
print("let's pause")
userInput = input()

# open for writing
# with open("testfile.csv", 'a') as f:
#     f.write(str(pcTime + "," + osType + "," + os_name))

# print("read as text file\n")
# with open('testfile.csv', 'r') as f:
#     print(f.read())
    
print("read as CSV file\n")
import csv
# exampleFile = open('testfile.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)

### NICER OPENING
def readCSVFile():
    with open(fileName, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)
# readCSVFile()

with open(fileName, mode='a') as file:
    writer = csv.writer(file)
    writer.writerow(data)



readCSVFile()


