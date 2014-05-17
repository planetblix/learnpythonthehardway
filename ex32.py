#!/bin/python

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list:" % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
   print "Element was: %d" % i 

#Study Drills
#1. range() definition: range(start,stop[,step])
#Interesting examples:
#>>> range(10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#>>> range(1, 11)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#>>> range(0, 30, 5)
#[0, 5, 10, 15, 20, 25]
#>>> range(0, 10, 3)
#[0, 3, 6, 9]
#>>> range(0, -10, -1)
#[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
#>>> range(0)
#[]
#You might think there is one element here, but if start > 0,
#then nothing further to do, result is empty list.
#>>> range(1, 0)
#[]

#2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?

#A good Guess: var0,var1,var2,var3,var4,var5 = range(0,6)
#Works on the command line.

#3. Other list functions other than append()
#list.append(x), apparently this is equiv. a[len(a):] = [x]
#list.extend(L), a[len(a):] = L
#list.insert(i,x), insert an item at a given position
#list.remove(x), remove the first item from the list whose value is x. Other it's an error
#list.pop([i]) - if no index, then removes the last item in the list.
#list.index(x) - Return the index of the list of the first item whose value is x. It is an error if there is no such item.
#list.count(x) - Return the number of times x appears in the list.
#list.sort() - sort the items of the list, in place.
#list.reverse() - reverse the elements of the list, in place. 
