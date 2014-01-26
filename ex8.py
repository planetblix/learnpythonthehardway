#!/bin/python

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
 	"But it didn't sing.",
	"So I said goodnight."
)

#Notes: Notice the line "But it didn't sing.",
#What is going on here?  Intepreter defaults to single quotes if there are no escape characters involved. See examples:
#>>> print "%r" % ("But it didn't sing.")
#"But it didn't sing."
#>>> print "%r" % ("But it didnt sing.")
#'But it didnt sing.'
#>>> print "%r" % ('But it didnt sing.')
#'But it didnt sing.'
#>>> print '%r' % ('But it didnt sing.')
#'But it didnt sing.'
#>>> print '%r' % ("But it didnt sing.")
#'But it didnt sing.'
