#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:44:13 2024

@author: marcus
"""

currentYear = 2024
# print(currentYear)
# print(type(currentYear))

loops= 0
name = input("What is your name? ")

print("Hello", name)
# ask the year of birth

year = input("What year were you born? ")

### If this, then that... 
## If not this... maybe that??

# if year.isdigit():
#     year = int(year)

while year.isdigit() == False:
    year = input("What year were you born? ")

year = int(year)
if year > 2024:
    print("THis")
elif year < 1900:
    print("That")
else:
    print("Come on... be reasonable")

# calcute your age... this year



# if the persons age is above 18 
# say they can go to the races

# if person below 13 years old - 
# must be with a responsible adult

# otherwise say you need to get 
# the parents permission
