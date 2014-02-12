#/bin/python

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Open the file..."
#rw doesn't mean read and write, it just means read!
#You could open the file twice, but not particularly safe,
#As you could overwrite the file.
target = open(filename, 'r+')

#Other file modes:
#'r'  - open for read only
#'r+' - open for read and write, cannot truncate
#'rb  - reading binary
#'rb+ - reading or writing a binary file
#'w'  - open for write only
#'w+' - open fo read and write, can truncate
#'a'  - open for append only
#'a+' - open for reading and writing.
#'U'  - opens file for input with Universal newline input.

#Based on C fopen(): http://www.manpagez.com/man/3/fopen/
#Nice examples here: http://www.tutorialspoint.com/python/python_files_io.htm

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write("%s\n" % line1)
target.write("%s\n" % line2)
target.write("%s\n" % line3)

print target.read()

print "And finally, we close it."
target.close()

