# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:32:49 2019

@author: 583435
"""
import itertools

def factors(my_num):
    for i in range(1, int(my_num)+1, 1):
        if(int(my_num)%i==0):
            yield i
        else:
            pass

def strArray(argArray):
    x=0
    y=1
    arr=[]
    while(x<len(argArray)-1 or y<len(argArray)-2):
        arr.append(str(argArray[x]) + str(argArray[y]))
        x=x+1
        y=y+1
    return arr
    
def compare(orgArr, argArr):
    for x in range(0, len(orgArr), 1):
        for y in range(0, len(argArr), 1):
            if(orgArr[x]==argArr[y]):
                return False
            else:
                pass
    return True
    
t=input("TestCases Count: ")
countResult=[]
while(int(t)>0):
    factNum = input("Enter any number of your choice\n")
    factArr=[]
    for x in factors(factNum):
        factArr.append(x)
    #print(factArr)
    
    resultList=list(itertools.permutations(factArr))
    
    orgArrayStr=strArray(factArr)
    finalArr=[]
    count=0
    eachset=False
    for ls in range(0, len(resultList), 1): 
        tempArr=strArray(resultList[ls])
        eachset=compare(orgArrayStr, tempArr)
        if(eachset):
            #print(tempArr)
            finalArr.append(resultList[ls])
        else:
            pass
            #print(tempArr)
    #print(len(finalArr))
    count=len(finalArr)
    countResult.append(count)
    t=int(t)-1
#print(countResult)
for c in countResult: 
    print(c)