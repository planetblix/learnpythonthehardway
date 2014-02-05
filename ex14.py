#!/bin/python

from sys import argv

script, user_name, phone_no = argv
prompt = '>>>'

print "Hi %s, I'm the %s script and your phone number is: %s" \
       % (user_name, script, phone_no)

print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "Is this definitely your phone number %s?" % phone_no
confirm = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r. about liking me.
You live in %r. Not sure where that is.
You said also said %s when confirming your phone number. Thanks.
And you have a %r computer. Nice.
""" % (likes, lives, confirm, computer)

#Zork and Adventure
#http://en.wikipedia.org/wiki/Zork
#That last % format activator allows variables to be inserted in order of the format specifiers in a multiline string. Cool.
