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
#Ex.3
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

"""
Ex.4 Factorial of Number
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
"""

"""
#Ex.5 - Performance of List Comprehension and Generators
import datetime

def getSquare(num):
    length = int(num)
    for i in range(1, length,1):
        yield i*i

print(datetime.datetime.now())
f2 = [0, 1]
for x in range(500000):
    #f1 = [i**2 for i in range(1, 21)]
    del f2[:]
    for count in getSquare(20):
        f2.append(count)    
#print(f1)
print(f2)
print(datetime.datetime.now())
"""



"""
#Ex.6 - Palindrome for a String
def isPalindrome(num):
    revStr = num[::-1]
    if(revStr == num):
        return True
    return False

myRes = isPalindrome('121215')
print(myRes)
"""


#Ex.7 - BlackJack Game logic 
def blackjack(a,b,c):
    add= sum([a,b,c]);  #sum function accepts a tuple input
    if add<=21: 
        return add
    #Check with Subtract 10 as return should be less than 21
    elif (a==11 or b==11 or c==11) and (add-10<=21): 
        return add-10
    else: 
        return 'BUST'