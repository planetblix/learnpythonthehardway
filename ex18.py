#!/bin/python

# this one is like your scripts with argv
#def - this is a Python keyword for making a function
#print_two - name of the function, a short name...
#that says what it does.
#*args (asterisk args) - similiar to argv but inside
#parentheses for this concept to work.
#: - the first line of the function ends with colon
#then indent 4 spaces, and unpack args
#finally print using the raw representation
def print_two(*args):
   arg1, arg2 = args
   print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
   print "arg1: %r, arg2: %r:" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
   print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
   print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
