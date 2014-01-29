tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# List of all Python escape sequences and an example use

# \\ Backslash
print "This is a backslash: \\"
backslash = "\\"
print "This is also a backslash: %s" % backslash
print "This is also a backslash, but in its raw form: %r\n" % backslash

print "This is a single-quote: \'"
singlequote = "\'"
print "This is also a single quote: %s" % singlequote
print "This is a also a singlequote, but in its raw form %r\n" % singlequote

print "This is a double-quote: \""
doublequote = "\""
print "This is also a double-quote: %s" % doublequote
print "This is also a double-quote: %r" % doublequote

print "This is a ascii-bell (BEL): \a"
asciibell = "\a"
#Note: This line DOES sound a bell.
print "This is also a ascii bell: %s" % asciibell
#Note: This line doesn't sound a bell.
print "This is also a ascii bell: %r" % asciibell
#Interesting, the string 'test' prints 'test'.
print "This is a ascii bell in the middle of a string: te%sst" % asciibell

print "This is a ascii backspace (BS): \b"
asciibackspace = "\b"
print "This is a ascii backspace: %s" % asciibackspace
print "This is a ascii backspace: %r" % asciibackspace
#Interesting, the 'e' disappears 
print "This is a ascii backspace: te%sst" % asciibackspace

print "This is a ascii formfeed (FF): \f"
asciiformfeed = "\f"
print "This is a ascii formfeed: %s" % asciiformfeed
print "This is a ascii formfeed: %r" % asciiformfeed
print "This is a ascii formfeed: te%sst" % asciiformfeed

print "This is a ascii linefeed (LF): \n"
asciilinefeed = "\n"

#Compare ''' with """ - notice the double and single quotes
print '''
This is a double-quote: "%s" 
This is a ascii-bell: "%s"
This is a ascii-formfeed: "%s"
This is a ascii-linefeed: "%s"
''' % (doublequote,asciibell, asciiformfeed, asciilinefeed)
print """
This is a double-quote: "%s" 
This is a ascii-bell: '%s'
This is a ascii-formfeed: '%s'
This is a ascii-linefeed: '%s'
""" % (doublequote,asciibell, asciiformfeed, asciilinefeed)



