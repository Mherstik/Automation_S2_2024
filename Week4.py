#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:04:48 2024

@author: marcus
"""


balance = 200

# step 1 – get the pin or exit
def get_pin():
    error_count = 0
    card_pin = 1234
    user_pin = ''
    # while user_pin != card_pin
    while user_pin != card_pin:
        user_pin = input("Give me your pin: ")
        if user_pin.isdigit():
            user_pin = int(user_pin)
    #     read user_pin
    #     if user_pin  = card_pin
        if user_pin == card_pin:
    #     exit loop
            break

    # else if user_pin != card_pin
        else:
    # increase error count
            # error_count = error_count + 1
            error_count += 1
    # if error_count = 3
            if error_count == 3:
                # eat card!!
                print("Too many pin attempts.\nContact bank for card")
                exit()
                # end program

get_pin()

def get_balance():
    global balance
    print(balance)

get_balance()


print("End of code!")
