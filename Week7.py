#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:11:55 2024

@author: marcus
"""



# CREATE A FILE
# Option 1
filename = "file2.txt"

# open file for writing
file = open(filename, 'w')

# write content
file.write("WHAT!?")

# close the file
file.close()

# Option 2
with open(filename, 'w') as file:
    file.write("This is content from with")
    

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