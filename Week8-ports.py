#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:14:50 2024

@author: marcus
"""

import psutil

def getActivePorts():
    active_ports = []
    connections = psutil.net_connections(kind='tcp4')  # Fetch TCP connections
    for conn in connections:
        if conn.status == 'LISTEN':
            active_ports.append(conn.laddr.port)
    return active_ports

portListen = getActivePorts()
portEstab = []

connectList = psutil.net_connections(kind='tcp4')
for each in connectList:
     if each.status == 'ESTABLISHED':
        portEstab.append(each.laddr.port)

print(len(portListen), len(portEstab))

# print(port_list)
# port_list = psutil.net_connections()
# for port in port_list:
#     print(port[:4])   # this shows the list of ports
#     i = i + 1
#     if i == 3:
#         break
# print(len(portList))  ## this shows how many items in the list