#!/bin/python

#Assigns integer 100 to the variable cars
cars = 100
#Assigns floating point 4.0 to variable space_in_a_car
space_in_a_car = 4.0
#Assigns the value 30 to the variable 30
drivers = 30
#Assigns the value 90 to the variable  passengers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

