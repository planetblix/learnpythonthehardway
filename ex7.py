#!/bin/python

#Just a normal python string. I accidently put . after the double quotes
print "Mary had a little lamb."
#'snow' is actually a string, not a variable as you might think. Python idiom seems to be use single quotes for short strings.
print "Its fleece was white as %s." % 'snow'
#Just a normal python string
print "And everywhere that Mary went."
#This prints whatever is between the double quotes, ten times
print "." * 10 #what did that do

#endX is just a variable name, not an instruction
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch  that comma at the end. try removing it to see what happens
# this line concatenates each of those variables.
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#Notes:
#That comma at the end seems to eliminate the newline character. I noticed this when I removed the comma.
#Code taking up more than 80 lines is bad Python style!
