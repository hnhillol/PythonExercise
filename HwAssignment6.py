# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 00:43:26 2019

@author: hnhillol
Homework Assignment #6: Advanced Loops
Create a function that takes in two parameters: rows, and columns, both of which are integers. 
The function should then proceed to draw a playing board (as in the examples from the lectures) 
the same number of rows and columns as specified. After drawing the board, your function should return True.
Extra Credit:
Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. If someone passes a value greater than either maximum, your function should return Talse. 

"""

import shutil 

maxRows = shutil.get_terminal_size().columns # Width
maxCols = shutil.get_terminal_size().lines   #Height

print ("Maximum Rows :" , maxRows,", Maximum Coloumns :" ,maxCols)

def PlayingBoard(rows,columns):
 if rows<=maxRows and columns<=maxCols and rows%2==1 and columns%2==0:
    for row in  range (rows):
        #0,1,2,3,4
        if row % 2 ==0:
            for column in range (1,columns):
                if column % 2 == 1:
                    if column != columns-1:
                        print(" ",end="")
                    else:
                        print("")
                else:
                    print("|" , end ="")       
        else:
            print("-"*(columns-1))
    return True
 else :
     print ("Condition Denied !!")
     return False 
 
    
 
rows=int(input("Enter the number of rows (It should be integer,odd and <= Maximum Rows): "))
columns=int(input("Enter the number of coloumns (It should be integer,even and <=Maximum Coloumns): "))
print(PlayingBoard(rows,columns))   








 
        