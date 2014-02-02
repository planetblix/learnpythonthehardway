#!/bin/python

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#Other ways to use the built-in raw_input()
#Ref: http://docs.python.org/2.7/library/functions.html#raw_input
#1. The line below doesn't use a trailing newline. That is, '--->' will print and then on the same line, you can type your input
s = raw_input('--->')

#2. Useful for choices like C switch statements, but in Python can use a combination of if/elif/else statement
#Ref: http://www.cyberciti.biz/faq/python-raw_input-examples/

#Get input
choice = raw_input('Enter your choice [1-3] : ')
#The second choice below is actually a string, needs converting
choice = int(choice)

if choice == 1:
	print ("Lettuce...")
elif choice == 2:
	print ("Tomato...")
elif choice == 3:
	print ("Rebooting the cucumber...")
else:
	print ("Invalid number. Try again...")

#In reality, we should use try/catch, but more on that in a later exercise

#3.  raw_input() isn't available in Python 3.



#Notes:
#The comma at the end of the print line doesn't end the line with a newline character.


