

# This is the function, it takes 2 arguments which can be defined, called or manipulated as required.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d chseese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# Here we call the function and give values to the arguments within the ()
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# Here we define the variables in the script 
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Then call the function and pass them through the function's ()
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This is an example of calculations being used as arguments () 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Finally we can mix globaly defined variables with equations to define the arguments being passed to the function.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

"""
Study Drills

1. Explian the script

2. Read the code backwards saying all the important characters.

3. write aonother function running it 10 different way... ex19a.py

"