#!/bin/python

days = "Mon Tue Wed Thu Fri Sat Sun"
#Jan doesn't start on a newline? why? Needs \n at beginning.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

#This is one to remember, start with """ and end with """ for printing multiple lines.
print """
There's something going on here.
With the three-double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
