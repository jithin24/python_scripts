# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 19:50:14 2019

@author: 583435
"""
import textwrap

def divideStr(string, inp):
    searchList=textwrap.wrap(string, int(inp))
    return searchList

def compare(arr):
    for a in range(0, len(arr), 1):
        for b in range(a+1, len(arr),1):
            if(arr[a]==arr[b]):
                #print(True)
                return arr[a]
            else:
                pass
inpSet=input("Enter the sequence length\n")
inputSeq= input("Enter the Sequence\n")
lenStr=len(inputSeq)
result=set()
for i in range(0, lenStr, 1):
    pass
    #print(divideStr(inputSeq[i:]))
    result.add(compare(divideStr(inputSeq[i:], inpSet)))
    #print(result)
    
for r in result:
    if(r is not None):
        print(r)