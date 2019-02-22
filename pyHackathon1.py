# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:42:31 2019

@author: 583435

Python Hackathon Challenges
"""

def FirstFactorial(num): 

    # code goes here 
    fact=1
    while(num>=1):
        fact*=num
        num=num-1
    return fact

#inp=input("Enter the Number for Factorial")
#print(FirstFactorial(int(inp)))

"""
arr=['F','G','H','I','J','K','L','M','N','O','P']
genArr=(ord(x) for x in arr)
for x in genArr:
    print(x)


Value Compare Game    
a=[2, 3, 5]
b=[5, 1, 7]
aPt=0
bPt=0
for i in range(0,3):
    if(a[i]>b[i]):
        print(a[i])
        aPt+=1
    elif(a[i]<b[i]):
        print(b[i])
        bPt+=1
    else:
        pass
print(str(aPt)+" "+str(bPt))

""" 

"""
Summation of Long Int Array
add=0
numArr=[1000000001,1000000002,1000000003,1000000004,1000000005]
for x in range(0,len(numArr)):
    add+=numArr[x]
print(add)
"""


"""
Diagonal Summation

arr=[
     [11, 2, 4],
     [4, 5, -6],
     [10, 8, -12]
    ]
#print(len(arr));

primDiagonal=0
secnDiagonal=0
secLen=len(arr);
for x in range(0,len(arr)):
    for y in range(len(arr[x])):
      if(x==y):
          primDiagonal+=arr[x][y]
    secnDiagonal+=arr[x][secLen-1]
    secLen-=1
print(primDiagonal)
print(secnDiagonal)
print(abs(primDiagonal-secnDiagonal))
"""

"""
Average
numArr= [-4,3,-9,0,4,1]

pos, neg, zero= 0,0,0
for num in numArr:
    if(num>0):
        pos+=1
    elif(num<0):
        neg+=1
    else:
        zero+=1
    
print(round(pos/len(numArr), 6))
print(round(neg/len(numArr), 6))
print(round(zero/len(numArr), 6))
"""

"""
Pattern
     #
    ##
   ###
  ####
 #####
######


n=6
height=n
for m in range(0,n,1):
    for k in range(0,height,1):
        if(k==height-1):
            print('#'*(n-k))
        else:
            print(' ', end ="")
    height=height-1
"""

"""
#Min Max Sum
minSum,maxSum=0,0
arr=[7, 4, 8, 3, 9, 18, 5]
arr.sort()
for x in range(0, len(arr), 1):
    if(x==0):
        print(arr[x])
        minSum+=arr[x]
    elif(x==len(arr)-1):
        print(arr[x])
        maxSum+=arr[x]
    elif(x!=0 and x!=len(arr)-1):
        print(arr[x])
        minSum+=arr[x]
        maxSum+=arr[x]
    else:
        pass
print(minSum)
print(maxSum)
"""

"""
ar=[2, 5, 1, 3, 5, 0, 5, 2]
max=0
for x in range(0, len(ar), 1):
    if(ar[x]>max):
        max=ar[x]
    else:
        pass
print(ar.count(max))
"""

"""
#Time Analysis

timeStr="00:00:00AM"
hr=timeStr[:2]
mr=timeStr[-2:]
unchanged=timeStr.strip(hr).strip(mr)

if(int(hr)==12 and mr=="AM"):
    hr='00'
elif(int(hr)==12):
    pass    
elif(mr=="PM"):
    hr=12+int(hr)
print(str(hr)+unchanged)
"""


