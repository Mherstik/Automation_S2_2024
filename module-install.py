#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:09:03 2024

@author: marcus
"""

#Here's how you can check if a Python module is installed and install it if it is not:

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_install(package):
    try:
        __import__(package)
        print(f"{package} is available")
    except ImportError:
        print(f"{package} not available.\nInstalling now...")
        install(package)

# Example usage:
# check_install("psutil")
# check_install("speedtest-cli")

packageList = ['uuid','psutil', 'speedtest-cli', 'pandas']

for package in packageList:
    check_install(package)

# Import the modules after ensuring they are installed
import psutil
import speedtest
import pandas
import uuid

# ### Explanation:
# 1. **Install Function**: The `install` function uses `subprocess.check_call` to call `pip` and install the specified package.
# 2. **Check and Install Function**: The `check_install` function tries to import the package. If an `ImportError` occurs, it calls the `install` function to install the package.
# 3. **Example Usage**: The script checks for `psutil` and `speedtest-cli` modules and installs them if they are not already installed.

# This code snippet ensures that the required modules are installed before using them, making your script more robust and portable. Would you like to know more about how this works or need help with something else?

# (Stolen from CoPilot)