#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:53:19 2024

@author: marcus
"""


import psutil
import csv
import time
import os
import platform
import sys

my_system = platform.uname()

#print(f"System: {my_system.system}")
#print(f"Node Name: {my_system.node}")

currentTime = time.ctime()

hostName = my_system.node
# print(hostName)
sysName = my_system.system

def getActivePorts():
    active_ports = []
    connections = psutil.net_connections(kind='tcp4')  # Fetch TCP connections
    for conn in connections:
        if conn.status == 'LISTEN':
            active_ports.append(conn.laddr.port)
    return active_ports

portListen = getActivePorts()
portListen = str(portListen).strip('[]').replace(',', ';')

fileName = input("Gimme a filename: ")
isFile = os.path.isfile(fileName)


header = ['Time','hostname', 'sysname', 'ports']
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


data = [currentTime, hostName, sysName, portListen]

def write2CSV(data):
    with open(fileName, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow(data)


### NICER OPENING
def readCSVFile(data):
    with open(fileName, mode='r') as file:
        csvFile = csv.reader(file)
        # for lines in csvFile:
        #     print(lines)

        i = 1
        for row in csvFile:
            # print(f"checking row {i}")
            hostCheck = row[1]
            sysNameCheck = row[2]
            # print(macCheck)
            if hostCheck == hostName and sysNameCheck == sysName:
                print(f"Row {i} has a {hostCheck} & {sysName} is a match!")
                ##
                # ask if they want to exit
                cont = input("Do you want to exit [Y/n]: ")
                if cont.lower() == 'y':
                    sys.exit()
               
            i = i + 1
        write2CSV(data)
            # else:
            #     print("no match")
           
readCSVFile(data)







