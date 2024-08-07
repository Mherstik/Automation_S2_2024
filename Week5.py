#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:04:48 2024

@author: marcus
"""
import sys

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
                sys.exit()
                # end program



def get_balance():
    global balance
    return balance


def transaction():
    global balance

    # ask deposit or withdrawl
    options = ''

    while options.lower() != "x":
        options = input("Would you like to do:\n[1] Deposit or \n[2] Withdraw \nX to exit: ")
        
        if options.lower() == "x":
            sys.exit()
        
        else:
            # ask how much
            amount = int(input("How much are you wanting: "))

            if int(options) == 1:
                balance = balance + amount

            
            elif int(options) == 2:
            # if withdrawl - check if there's enough
                # if there's enough, give money & reduce balance
                # if not enough, say sorry, you don't have enough
                if amount > get_balance():
                    print("You don't have enough money")
                    print("You have $" + str(get_balance()), "available")
                else:
                    balance = balance - amount
                
            else:
                print("invalid option")
            
        print("Your balance is $"+ str(get_balance()))
        ## Continue?
        print("Do you want to continue?")
        cont = input("y/N: ")
        if cont.lower() == "y":
            continue
        else:
            sys.exit()
    
    # if deposit - increase balance by amount

get_pin()    
print(get_balance())
transaction()


print("End of code!")
