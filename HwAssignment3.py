# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:43:50 2018

@author: hnhil
Details:
 
Create a function that accepts 3 parameters and checks for equality between any two of them. 

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.


Extra Credit:

Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function:

6,5,"5"

You should modify it so that it returns true instead of false. 

Hint: there's a built in Python function called "int" that will help you convert strings to Integers.

"""

def Check(x,y,z):
    
    if int(x)==int(y) or int(y)==int(z) or int(z)==int(x):
        return True
    else :
        return False

      
result =Check("10",10,5)

print(result)
    
    
    