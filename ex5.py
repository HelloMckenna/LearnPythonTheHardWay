name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
centimeters = 2.54
kilograms = 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall. That's %d in centimeters." % (height, height * centimeters)
print "He's %d pounds heavy. Thats %d in kilograms." % (weight, weight * kilograms)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
