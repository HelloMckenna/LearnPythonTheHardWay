age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("how much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)


#1. In Terminal where you normally run python to run your scripts, type pydoc raw_input.
#   Read what it says. If you're on Windows try python -m pydoc raw_input instead.

# help(raw_input) does work

#2. Get out of pydoc by typing q to quit.
#3. Look online for what the pydoc command does.

# The built-in function help() invokes the online help system in the interactive interpreter,
# which uses pydoc to generate its documentation as text on the console.
# The same text documentation can also be viewed from outside the Python interpreter by running
# pydoc as a script at the operating system's command prompt.

#4. Use pydoc to also read about open, file, os, and sys.
# run
#help(open)
#help(file)
#help(os)
#help(sys)


#It's alright if you do not understand those; just read through and take notes about interesting things.