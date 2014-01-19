#!/bin/python

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %d inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %s." % (age, height, weight, age + 
height + weight)

#Notes:
#Discussion between %r and %s: http://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python
#basically %s converts the object using str()
#%r converts the object using repr()
#for %r strings return in single quotes, but differs depending on types
#%r is useful for debugging, displays the raw data of the variable.

