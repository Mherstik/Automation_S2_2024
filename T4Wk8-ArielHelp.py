#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:14:50 2024

@author: marcus
"""

import psutil
import csv
import time
import os

currentTime = time.ctime()

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


header = ['Time', 'ports']
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


data = [currentTime, portListen]

### NICER OPENING
def readCSVFile():
    with open(fileName, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)

with open(fileName, mode='a') as file:
    writer = csv.writer(file)
    writer.writerow(data)



readCSVFile()












#####################
# portEstab = []
# portAll = []

# connectList = psutil.net_connections(kind='tcp4')
# for each in connectList:
#      if each.status == 'ESTABLISHED':
#         portEstab.append(each.laddr.port)

# connectList = psutil.net_connections(kind='tcp4')
# for each in connectList:
#      portAll.append(each.laddr.port)


# print(len(portListen), len(portEstab), len(portAll))
# print(portListen, "\n", portEstab, "\n", portAll)
# print(port_list)
# port_list = psutil.net_connections()
# for port in port_list:
#     print(port[:4])   # this shows the list of ports
#     i = i + 1
#     if i == 3:
#         break
# print(len(portList))  ## this shows how many items in the list