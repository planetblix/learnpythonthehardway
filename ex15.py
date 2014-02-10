#This is a shebang (informally), aka. intepreter directive. The program is instructed to run python instead of the default shell. python has to be specified as an absolute path. Read discussion here: http://en.wikipedia.org/wiki/Shebang_(Unix)
#!/bin/python

#We're going to use the argv from the sys module
from sys import argv

#This is iterable unpacking, only on iterable types. Python 3 allows extended iterable unpacking.
script, filename = argv

#open() returns a file object
txt = open(filename)

#Using the object named filename (unpacked by argv), print the value assigned to 'filename'
print "Here's your file %r:" % filename
#file object has functions! Check what other functions there are.
#read() this returns the entire contents of the file as a string.
#Watch out if the file is huge, read(size) can limit the read.
#This is different to readline(), this just read's one line, and
#a newline i.e. \n is appended to the string, except the last line!
#Source: http://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
print txt.read()

print "Type the filename again:"

#raw_input reads a line from input, converts it to a string, the ">" it's just
#written to the standard output i.e. command line, before the prompt.
file_again = raw_input(">")

#open returns a file object, infact using C's stdio package.
txt_again = open(file_again)

#same description as above but different file object.
print txt_again.read()

#Notes: Other file object functions

#fileno(...) returns a file descriptor
fileno = txt.fileno()
print fileno;

#flush() flush the internal buffer
txt.flush()

#isatty() checks if the file is connected to a tty device
atty=txt.isatty()
print atty

#next()
#read()
#readinto()
#readLine()
#readLines()
#seek()
#tell()
#truncate()
#write()
#writeLines()
#xreadLines()

#Remember to close files
txt.close()
txt_again.close()
