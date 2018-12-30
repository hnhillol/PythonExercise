# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 00:56:34 2018

@author: hnhil
"""

def isPrime(number):
    x = True 
    for i in range(2, number):
       if number%i == 0:
           x = False    
    return x
      
   
def fizzBuzz(number):
    if number%3==0 and number%5==0:
        print ("FizzBuzz")
    elif number%3 ==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:      
        print(number)
                

for number in range(1,101):
    if number>1 and isPrime(number)== True:  #Prime Number is Always >1 , only Divide by itself and 1 
        print("Prime")  
    else:
        fizzBuzz(number)
    
