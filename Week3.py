#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:20:56 2024

@author: marcus
"""

# a = 5
# b = 2

# print(a/b)
# print(a%b)  # remainder
# print(a//b) # modulus = whole times it fits
# print(a**b)
# print(a*b)

# print((int(21** 0.5 )+1))

###
# Check number from 2 --> int(num ** 0.5 +1)
#    if number remainder from each number is 0 
#        then the number is not a prime



userInput = int(input("Choose a number: "))
# if a == 2:
#     print("It's TRUE")

## Ask what direction are we going?
choice1 = input("What to convert from F or C? ")

## take input and convert
# celcius = (farenheit - 32) * 5/9
def convertF2C():
    print(((userInput -32) * 5 / 9 ), "C")

# farenheit = celcius * 9/5 + 32
def convertC2F():
    print(((userInput * 9/5) + 32) ,"F")

if choice1 == "F":
    #convertF2C()
    print(((userInput -32) * 5 / 9 ), "C")

elif choice1 == "C":
    #convertC2F()
    print(((userInput * 9/5) + 32) ,"F")




######################3
## Prime Checker

# def isPrime(num):
#     # check if number less than 2
#     if num < 2:
#     # and give back a false
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# if isPrime(userInput) == True:
#     print("It's a prime")
# else:
#     print("Not a prime")
    