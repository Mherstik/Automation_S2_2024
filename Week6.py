#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:20:01 2024

@author: marcus
"""


def numberCheck(num):
        try:
            float(num)
            return True
        except ValueError:
            return False
        
print(numberCheck(12))
print(numberCheck("Test"))
print(numberCheck(14.2))
print(numberCheck("-2"))
print(numberCheck("-2.5"))

# num = "test"
# print(int(num))

# import random

# random_number = random.randint(1, 6) 
# print(random_number)


# def debugger(x, y):
#     breakpoint()
#     result = x / y
#     return result

# print(debugger(5, 0))


# import logging
# x = 5
# y = 0

# logging.warning("This is a warning")


# x = 1.2
# y = 0
# try:
#     print("Division", x/y)
# # except ZeroDivisionError:
# #     print("Division by zero is not possible")
# # except TypeError:
# #     print("Wrong types buddy")
# except :
#     print("Generic error message")
# #print("Division", x/y)


