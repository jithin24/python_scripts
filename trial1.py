# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:27:57 2018

@author: 583435
Practise programs in Python
"""

"""
#Ex.1

def numFactorial(num):
    if(int(num) == 0):
        return 1
    else:
        num = int(num) * numFactorial(int(num)-1)
        return num

numInp = input("Enter any number of your choice ")
numInp = abs(int(numInp))
print(numFactorial(numInp))
"""

"""
#Ex.2
class inputOutString(object):
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Enter any Number ")
    
    def printString(self):
        return self.s.upper()

strObj = inputOutString()
strObj.getString()
print(strObj.printString())
"""

"""
# A simple generator function
def py_gen():
    print("Launch Function")
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    print('=== Exit ===')
    yield n

# Using for loop
for item in py_gen():
    print(item)  
"""

"""
def rev_str(my_str):
    print(my_str)
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)
"""
    
def printNum(my_num):
    print(my_num)
    length = int(my_num)
    for i in range(length, 0,-1):
        yield i

factNum = input("Enter any number of your choice ")
num = 1
for count in printNum(factNum):
    print(count)
    num = num * count
print(num)