print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#Study Drills
#1. Go online and find out what Python's raw_input does.
#2. Can you find other ways to use it? Try some of the samples you find.
#3. Write another "form" like this to ask some other questions.
#4. Related to escape sequences, try to find out why the last line has '6\'2"' with that
#   \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?

#1. raw_input() Requests an input line from the user, converts it into a string and returns it
#2. You can use it to calcualte math or create a unit converter... Fill in forms etc!
#3.

print "Where do you work?",
work = raw_input()
print "What is your favorite colour?",
colour = raw_input()
print "Do you know the answer to 2 + 2? What is it?",
answer = raw_input()


print "So, you work in %s" % work
print "Your favorite colour is %s" % colour
print "And you think that 2 + 2 = %s" % answer

#4 DO NOT KNOW