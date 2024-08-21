#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:11:55 2024

@author: marcus
"""

import os.path

balanceFile = "balance.txt"
# does the file exist
# option 1 - is file
# only checks files
if os.path.isfile(balanceFile):
    print("File's there")
    with open(balanceFile, 'r') as file:
        balance = file.read()
        print(f"You have ${balance}")
else:
    print("That file is missing, creating")
    with open(balanceFile, 'w') as file:
        file.write("0")
        balance = "0"

## out of the file stuff
# print(f"Out of the file stuff ${balance}")
#print(type(balance))
balance = int(balance)

## Pass go - get 200

balance = balance + 200
print("Add 200 for passing GO")

with open(balanceFile, 'w') as file:
    file.write(str(balance))
    
with open(balanceFile, 'r') as file:
    balance = file.read()
    print(f"You have ${balance}")

# option2 - exists
# if os.path.exists(balanceFile):
#     print("Something exists there")
# else:
#     print("That thing is missing")






# # CREATE A FILE
# # Option 1
# filename = "file2.txt"

# # open file for writing
# file = open(filename, 'w')

# # write content
# file.write("Write first")

# # close the file
# file.close()

# # Option 2
# with open(filename, 'r+') as file:
#     print("The file said", file.read())
#     print("Move to start of file")
#     file.seek(0)
#     print("The start said", file.read())
#     file.write("This is a+ from with")
#     print("Move to start of file again")
#     file.seek(0)
#     print(file.read())
    
# with open(filename, 'r') as file:
#     print(file.read())

####

# # Open a file
# filename = "File1.txt"

# # File_object = open(r"File_Name", "Access_Mode")

# # f = open(r"C:\Documents\temp\filename.txt")
# f = open(filename, "r")

# # with open("file1.txt", w) as f1:
# #     f1.write

# # Read contents
# print(f.read())


# # Close file
# f.close()