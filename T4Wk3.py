#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:15:11 2024

@author: marcus
"""
from time import time, ctime, gmtime
import os
import sys
import csv


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
#fileName = "testfolder"
fileName = "testfile.csv"
# isExists = os.path.exists(fileName)
# print(isExists)


isFile = os.path.isfile(fileName)
# print(isFile)
# isFile = os.path.isdir(fileName)
# print(isFile)


header = ['Time', 'ostype', 'osname']

def writeHeader():
    with open(fileName, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    print("Headers written.\nNow extracting data from PC")

if isFile == True:
    print("File exists")  #... extracting data from PC")
    fileKeep = input("Want to Delete or Continue (C/D)?")
    if fileKeep.upper() == "D" or fileKeep.upper() == "DELETE":
        print("Deleting file")
        os.remove(fileName)
        writeHeader()
    else:
        print("Continuing")
else:
    print("File not found... writing headers.")
    writeHeader()
    

# data = [str(pcTime + "'," + osType + "," + os_name)] # incorrect data type of string
data = [pcTime, osType, os_name]
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


