# From the system package import argument variable 
from sys import argv

# argv = the script name and filename (file name entered as part of the argument variable)
script, filename = argv

# Defining variable txt as the contents of the file defined in the argv
txt = open(filename)

# print string containing the file name of the file included in the argv
print "Here's your file %r:" % filename
# print the contence of the file named in the argument variable using the .read() function
print txt.read()

# requesting user input to create a file object using raw_input(). This can be any other file.
print "Type the filename again:"
file_again = raw_input(">")

# defining the raw_input() file object as file  a new variable
txt_again = open(file_again)

# printing the contents of the file object defined in the raw_input()
print txt_again.read()


"""
1: describe what each line does
2: python open - GOOGLE IT
open(name[, mode[, buffering]])
3: difference between commands functions and methods?

4: Get rid of the lines 10-15 where you use raw_input and run the script again. Means file is called by raw_input() rather than defined in the argv?

5: see ex15_exp.py for example of using just raw_input() to call and print a file.

"""