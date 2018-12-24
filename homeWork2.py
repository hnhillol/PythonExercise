# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:36:45 2018

@author: hnhil

These piece of codes  are to understand Functions and its uses. 
"""

def songDetails ():
    SongName= "Here comes the Sun" # First line of the song
    BandName="The Beatles" # The famous Band of the '70s
    SongDetail="Song Name: "+SongName+"  Band: "+BandName
    return SongDetail

def Artist():
    artist="John Lennon"
    return artist

def ReleasedYear():
    year=1969
    return year 

def EnglishSong():
    return True
    

song= songDetails ()
print (song)
artist=Artist()
print ("Artist Name: " +artist)
release=ReleasedYear()
print ("Release Year : ")
print(release)
Language=EnglishSong()
print("Is this a English Song ?")
print (Language)



    



