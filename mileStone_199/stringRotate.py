# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:31:50 2019

@author: 583435
"""

def getShiftedString(s, leftShifts, rightShifts): 
    tempString=str(s)
    # slice string in two parts for left and right
    if(leftShifts>len(tempString)):
        l=leftShifts%len(tempString)
    else:
        l=leftShifts
        pass
    Lfirst = tempString[0 : l] 
    Lsecond = tempString[l :]
    lrotation=str(Lsecond + Lfirst)
    
    if(rightShifts>len(tempString)):
        r=rightShifts%len(tempString)
    else:
        r=rightShifts
        pass
    Rfirst = lrotation[0 : len(tempString)-r] 
    Rsecond = lrotation[len(tempString)-r : ] 
    finalStr=str(Rsecond + Rfirst);
    
    # now concatenate two parts together 
    #print ("Left Rotation : ", lrotation)
    #print ("Right Rotation : ", finalStr)
    
    return str(finalStr)
    
# Driver program 
if __name__ == "__main__": 
    input = 'abcdefgh'
    print(getShiftedString(input,22,85))