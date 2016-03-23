__author__ = 'ryan.mckenna'

# Here we define the variables, which in this case are stings.

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)


# Here we print variables x ("There are 10 types of people." using the DECIMAL format character d% for 10)
# And y ("Those who know binary and those who don't" Using the STRING format character s% in parts)

print x
print y

# Printing string variables using the %r (repr()) REPRESENTATION or RAW format character, this "prints no matter what" and the STRING
# format character %s

print "I said: %r." % x
print "I also said: '%s'." % y

# Defining further variables as a boolean operator "False".
# And, a string variable using the RAW format character within the string NB !!! NOT SURE WHAT THIS DOES !!!

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"


# Printing the joke variables using the modulo to connect the string and the boolean.

print joke_evaluation % hilarious

#Simple variables printed using a concatination.

w = "This is the left side of..."
e = "a string with a right side."

print w + e




# Study Drills
#1. Go through this program and write a comment above each line explaining it. DONE
#2. Find all the places where a string is put inside a string. There are four places. 5
#3. Are you sure there are only four places? How do you know? Maybe I like lying. The 5 string is empty
#4. Explain why adding the two strings w and e with + makes a longer string. It is concatonating