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




