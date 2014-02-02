#!/bin/python

#this import style serves two purposes
#1. Keeps your program small
#2. Documentaton too, as you specify the exact functions
#Think of argv as a feature.
from sys import argv


#unpacks arv and assigns to the four variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

x = raw_input("Let's have more input:")
y = raw_input()
z = raw_input()

print x,y,z
#Notes:
#This error below appears if we don't provide enough arguments:
#ValueError: need more than 3 values to unpack
#What is a ValueError?
#It's raised when a built-in operation or function receives an argument that has the 
#the right type but an inappropiate value, and the situation is not described
#by a more precise exception such as IndexError. See the Exception hierarachy here:
#http://docs.python.org/2/library/exceptions.html


