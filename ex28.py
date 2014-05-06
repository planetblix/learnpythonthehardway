#!/bin/python

print "1. %r" % (True and True)    # True
print "2. %r" % (False and True)   # False
print "3. %r" % (1 == 1 and 2 == 1)# False
print "4. %r" % ("test" == "test") # True
print "5. %r" % (1 == 1 or 2 != 1) # True NB. watch out for typing !==
print "6. %r" % (True and 1 == 1)  # True
print "7. %r" % (False and 0 != 0) # False
print "8. %r" % (True or 1 == 1)   # True
print "9. %r" % ("test" == "testing") # False
print "10. %r" % (1 != 0 and 2 == 1)  # False
print "11. %r" % ("test" != "testing")# True
print "12. %r" % ("test" == 1) # False
print "13. %r" % (not(True and False)) # True
print "14. %r" % (not(1 == 1 and 0 != 1)) # False
print "15. %r" % (not(10 == 1 or 1000 == 1000)) # False
print "16. %r" % (not(1 != 10 or 3 == 4)) # False
print "17. %r" % (not("testing" == "testing")) # False
print "18. %r" % (not(1==1 and not ("testing" == 1 or 1 == 0))) # False
print "19. %r" % ("chunky" == "bacon" and not(3 == 4 or 3 == 3)) # False
print "20. %r" % (3 == 3 and not ("testing" == "testing" or "Python" == "Fun")) #False

