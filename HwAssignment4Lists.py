# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 19:27:15 2018

@author: hnhil
Details:
 
Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list. Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList. If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it should not be added, and the function should return False;

Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.


Extra Credit:

Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.

"""

myUniqueList=[]
myLeftovers=[]

def UniqueList(a): 
    if len(myUniqueList)==0:
        myUniqueList.append(a)
        return True
    elif a not in myUniqueList:
        myUniqueList.append(a)
        return True
    else:
        leftOverList(a)
        return False
  
def leftOverList(b):
    myLeftovers.append(b)
    
    
#Adding Unique values to the list         
UniqueList(2)
UniqueList('A')
UniqueList(5)
UniqueList(3)
UniqueList(4)
UniqueList(0)
UniqueList(1)
#Testing Uniqueness and leftovers  
UniqueList('A')
UniqueList(5)
UniqueList(0)

print(myUniqueList)
print(myLeftovers)