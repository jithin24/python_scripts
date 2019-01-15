# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:04:50 2018

@author: 583435
"""

"""
#Ex.1 Fibonnaci Series with Python Generators
def calcNum(len):
    num1=0
    num2=1
    for i in range(0, int(len), 1):
        yield num1
        temp = num1
        num1 = num2
        num2 = temp + num2

fibSeries = []
fiblen = input("Enter the Fibonnaci series length: ")
for fibCount in calcNum(fiblen):
    fibSeries.append(fibCount)
print(fibSeries)
"""

"""
states = "Alaska,California,Michigan,Colorado,Pennsylvenia"
lsStates = states.split(',');
lsStates.sort()
print(lsStates)
"""

"""
from time import sleep

fw=open('test.txt','w')
fw.write('Hello World\n') 
fw.write('This is our new text file\n') 
fw.write('and this is another line\n') 
fw.write('Why? Because we can\n') 
 
fw.close()

sleep(5)

fr = open('test.txt','r')
print(fr.readlines())
fr.close()

"""

"""
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0) 
for x in gen_exp:
    print(x)
"""


def myfunc(inpString):
    tempList = []
    strLength=len(inpString)
    for pos in range(0,strLength,1):
        if pos%2 == 0:
            tempList.append(inpString[pos].upper())
            #print(inpString[pos].upper())
        else:
            tempList.append(inpString[pos].lower())
            #print(inpString[pos].lower())
    return ''.join(tempList)