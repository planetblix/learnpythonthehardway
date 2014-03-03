#!/bin/python
#argv is a feature from the sys module
from sys import argv

#unpacks argv into script, and then input_file
script, input_file = argv

#print_all module, takes one argument
#expecting a file object, and calls
#the read function reads in bytes, no arguments reads all data until EOF is reached

def print_all(f):
   print f.read()

#seek - sets the file's current position
def rewind(f):
   f.seek(0)

#readline - Read one entire line from the file. A trailing newline character is kept in the string (but may be absent when a file ends with an incomplete line. 
def print_a_line(line_count, f):
   print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

