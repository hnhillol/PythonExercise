# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 02:34:40 2019

@author: hnhillol
Homework Assignment #7: Dictionaries and Sets
Details:
Return to your first homework assignments, when you described your favorite song. Refactor that code so 
all the variables are held as dictionary keys and value. Then refactor your print statements so that 
it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.
Extra Credit:
Create a function that allows someone to guess the value of any key in the dictionary, and find out 
if they were right or wrong. This function should accept two parameters: Key and Value. If the key exists
 in the dictionary and that value is the correct value, then the function should return true. In all other 
 cases, it should return false.
"""

MyFavSong={"Song Name":"Here comes the Sun","Band Name":"The Beatles",
           "Artist":"George Harrison","Album" : "Abbey Road",
           "Publisher":"Harrisongs","Released Date":"26" ,"Release Months":"September","Release Year":"1969",
           "Recorded Period":"7th July-19th August","Genre":"Folk pop , Pop Rock","Length":"3.06","Lable":"Apple",
           "Writter":"George Harrison","Producer":"George Martin"}

print("Here is the song Data")
print("*********************")
for key in MyFavSong :
    print(key,":",MyFavSong[key])

print ("\n")
print("Cross Checking the input data")
print("*****************************")

def FindSongInfo(key,value):
    if key in MyFavSong:
        if MyFavSong[key]==value:
            print("You are Correct !!")
            return True
        else:
            print("Attribute Data is incorrect !!")
            return False 
    else:
        print("Attribute Doesn't Exist")
        return False
        
key=input("Please enter the Attribute to check: ")
value=input("Guess the Data of the Attribute: ")
print(FindSongInfo(key,value))            