#/bin/python

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#Notes: pydoc research
#Pydoc very versatile tool, lets see, can you remember what these do?
#pydoc -k <keyword>
#pydoc -p <port>
#pydoc -w <name>

#Ref: http://www.oreillynet.com/mac/blog/2005/10/programming_is_just_easier_wit.html
 
#pydoc raw_input
   # Read a string from standard input.  The trailing newline is stripped.
   # If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
   # On Unix, GNU readline is used if enabled.  The prompt string, if given,
   # is printed without a trailing newline before reading.

#pydoc open
    #Open a file using the file() type, returns a file object.  This is the
    #preferred way to open a file.  See file.__doc__ for further information.

#pydoc os
    #os - OS routines for Mac, NT, or Posix depending on what system we're on.

#pydoc sys
    #This module provides access to some objects used or maintained by the
    #interpreter and to functions that interact strongly with the interpreter.



