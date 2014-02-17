#!/bin/python

#http://blog.amir.rachum.com/blog/2013/10/10/python-importing/
#using os.path as an example
import os
import os.path
from os.path import exists
from os.path import exists, dirname
from os.path import *
from os.path import exists as here
from .os import exists
os.path = __import__("os.path")
reload(foo)

#import os
#-loads os module into memory
#-to view the directories that get searched for modules
#import sys
#print sys.path

#import os.path
#-imports the object os.path only, other objects are not accessible directly.

#from foo import bar
#-Here bar is an object, an object could be:
#function definition
#class
#submodule 

#from foo import bar, baz
#bar and baz can be different types

#from foo import *
#bad practice - contiminates the global namespace

#from foo import bar as fizz
#this makes a nice namespace when objects are similiarly spelt
#when importing from different modules 
#Also useful to rename object names, to maybe more meaingful ones

#from .foo import bar
#doesn't check PYTHONPATH if you've got a local copy of the module
#can also do ..foo import bar
#also ...foo import bar

#foo = __import__("foo")
#import a module dynamically, must be assigned to a variable
#to be accessible


