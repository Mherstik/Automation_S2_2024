#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:11:55 2024

@author: marcus
"""

# Open a file
filename = "File1.txt"

# File_object = open(r"File_Name", "Access_Mode")

# f = open(r"C:\Documents\temp\filename.txt")
f = open(filename, "r")


# Read contents
print(f.read())


# Close file
f.close()