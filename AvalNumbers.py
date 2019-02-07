# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:45:15 2019

@author: Kevin
"""

MyNumber = 1000
isAval = True 

print("listing Aval numbers smaller than " + str(MyNumber) + ": ")
for i in range(3,MyNumber+1):
    j = i-1  
    isAval = True
    while (j>1):
        if (i%j==0):
            isAval = False
            break
        else:
            j -= 1
            
    if (isAval == True):
        print(str(i) + ", ")
        
if (isAval == True):
     print("no number found")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            