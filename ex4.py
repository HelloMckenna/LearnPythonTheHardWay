# This is the number of cars available.
cars = 100

# This is the space available in each car.
space_in_a_car = 4

# This is the number of people that can drive the cars.
drivers = 30

# This is the number of passangers that need to be car pooled.
passengers = 90

# This is the number of cars that do not have drivers.
cars_not_driven = cars - drivers

# This is the number of cars with drivers.
cars_driven = drivers

# This is the number of placeas available to passangers needing a carpool.
carpool_capacity = cars_driven * space_in_a_car

# This is the average number of passangers per car in order to carry all the required passangers.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
