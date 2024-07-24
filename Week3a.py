#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:44:10 2024

@author: marcus
"""

## Choose your own adventure
# do you like movies or music
choice1 = input("Do you like movies or music: ")

## if they like movies - 
if choice1 == "movies":
    print("Movie lover")
    
### Action or comedy
    choice2 = input("Action or comedy")
    # if ???
    if choice2 == "action":
        print("You like action movies")
    # else ??
    else:
        print("You like comedy movies")

# if they like music
elif choice1 == "music":
    print("Music lover")

    ### classical or modern
    choice2 = input("Classical or modern? ")
    if choice2 == "classical":
        print("You like classical music")
        
    else:
        print("You like modern music")

else:
    print("Invalid option")