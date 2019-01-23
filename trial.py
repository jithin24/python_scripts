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


"""
Ex.2 
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
"""

"""
Ex.3 Python BootCamp Exercises

print("Binary- ", bin(1024))
print("Hex- ", hex(1024))
s = 'hello how are you Mary, are you feeling okay?'
print("Check if all lower- ", s.islower())

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print("Count of w- ", s.count('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

set3 = set1 | set2
print(set3)
print("Only in set 1- ", set3.symmetric_difference(set2))

print("Difference- ", set1.difference(set2))

print("Intersection :", set1 & set2)

list1 = [1,2,3,4]
list1.reverse()
print("reverse- ", list1)

dict = {x:x**3 for x in range(5)}
print("Dictionary- ", dict)

"""


"""
Ex.4 Handling Random words from dictionary File
Hangman Game
"""
import random

def display_word(p_word):
    print(p_word)

def set_letter(p_letter, pos):
    return [w.replace('_', p_letter.upper()) if (l==pos and w=='_') 
            else w for l,w in enumerate(guessList)]

fr=open('sowpods_dictionary.txt','r')
wdList=fr.readlines()
hangStr = random.choice(wdList)
#print('Total Words: ', hangStr)
hangList=list(hangStr)
hangList.pop()
#print(hangList) 
fr.close()

guessList = ['_']*len(hangList)
print("Let's start the Hangman Game\nYou have 10 shots to guess this one")
display_word(guessList)
score=100
inpSet=set({})
while(True):
    inp=input(f"Guess a Letter from this Word skip:{inpSet}\n")
    count_underscores=guessList.count('_')
    if(inp.lower()=='score'):
        print(score)
    else:
        inp_pos=lambda inp:[l for l,x in enumerate(hangList) if x==inp]
        pos_list=inp_pos(inp.upper())
        for p in pos_list:
            guessList=set_letter(inp,p)
        post_count_underscores=guessList.count('_')
        display_word(guessList)
        if(post_count_underscores==0):
            print(f'You win!!! Score:{score}')
            break
        elif(post_count_underscores<count_underscores):
            inpSet.add(inp)
            print('Found- Letter inserted')
        else:
            score -= 10
            inpSet.add(inp)
            print('Sorry! Not Found')
        if(score>0):
            pass
        else:
            print(f"You have exhausted your guess limit\nWord: {hangStr}")
            break