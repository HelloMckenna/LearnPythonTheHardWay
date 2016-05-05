# from the system package, import argument variable 
from sys import argv

# argv = The script name an file name (file name entered as part of the argument variable)
script, filename = argv

# print text string plus the file name
print "We're going to erase %r." % filename
#Gives oppotunity to escape the script using CTRL_C
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# opening the file (choosen in the exicution statement) using WRITE mode
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# Erasing the contents of the file
target.truncate()

print "Now I'm going to ask you for three lines."

# defineing three strings of text
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

#writing the variables defined using raw_input() to the file.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file... its good house keeping
print "And finally, we close it."
target.close()

