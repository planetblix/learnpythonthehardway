#!/bin/python

# x is being assigned the string on the right hand side of the equals; except to place a variable in the middle of a string, one way is to place format specifier in the correct place i.e. %d and then at the end of the string place a % sign followed by a variable name or the actual value. Space after % is optional
x = "There are %d types of people." %10
#Assigns the string "binary" to the variable (or object) binary
binary = "binary"
#Same as above but different string. Note the single quote, string just recognises it, some languages require escaping fancy characters. e.g. C
do_not = "don't"
#y is assigned a string, but contains two format specifers, more than one variables included in the string requires brackets.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#%r is for debugging i.e. the raw data
print "I said: %r." % x
#%s is for displaying to users, note the single quotes - what is it's purpose? 
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#This looks like a contanation...interesting!
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
