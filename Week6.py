#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:20:01 2024

@author: marcus
"""

newList = []
val = ''

while val != "x":
    val = input()
    newList.append(val)
    print(newList)


aList = ["server1",
          "server2",
          "server3", 
          "server4"]

print(len(aList))

print(aList[2])
print(aList[:2])

## this is a string
something = "This is something. It is really long"

count = 0
# for each in something:
#     print(each)
    

for each in something:
    if each == "t":
        count = count + 1
print(count)

print(something)

print(len(something))

# print(something[19:])
# print(something[:19])
# print(something[:-4])
# print(something[1:20:5])

# import random
# print(random.randrange(0,100,5))
# print(random.randrange(0,-66,-5))
# def numberCheck(num):
#     '''

#     Parameters
#     ----------
#     num : int or float
#         The input to check

#     Returns
#     -------
#     bool
#         True if a number
#         False is not a number.

#     '''
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False
    
    
    
# help(numberCheck)
# print(numberCheck())
# print(numberCheck(12))
# print(numberCheck("Test"))
# print(numberCheck(14.2))
# print(numberCheck("-2"))
# print(numberCheck("-2.5"))


# assert numberCheck("test") == True, "Should be True"
# assert numberCheck("test") == False, "Should be False"



# print("You are here")
# x = "hello"

# #if condition is False, AssertionError is raised:
# assert x == "goodbye", "x should be 'hello'" 

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


