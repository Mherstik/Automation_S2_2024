#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:49:46 2024

@author: marcus
"""

import subprocess
import re

def get_open_ports():
    try:
        # Execute the netstat command
        result = subprocess.run(['netstat', '-an'], capture_output=True, text=True, shell=True)

        # Check if the command was executed successfully
        if result.returncode != 0:
            print("Failed to execute netstat command.")
            return []

        # Parse the output
        open_ports = []
        lines = result.stdout.splitlines()
        
        for line in lines:
            # Look for lines containing a local address with a port
            match = re.search(r'\s+(\d+\.\d+\.\d+\.\d+):(\d+)', line)
            if match:
                port = match.group(2)
                open_ports.append(port)

        return list(set(open_ports))  # Return unique ports
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    ports = get_open_ports()
    print(ports)
    # if ports:
    #     print("Open ports found:")
    #     for port in sorted(ports):
    #         print(port)
    # else:
    #     print("No open ports found.")
