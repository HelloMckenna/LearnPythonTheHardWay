from sys import argv

script, filename = argv

print "What file are we going to read?"

text = raw_input(">")
print text.read()

print "lets make some changes to the file! Give me three lines to write to the file."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'll just open the file for writing"
raw_input("Hit RETURN to continue")

target = open(filename, 'w')

print "And truncate the contents!"
raw_input("Hit RETURN to continue")

target.truncate()

print "lets check it's empty..."
raw_input("Hit RETURN to continue")

print text.read()

print " now I will write the three lines to file."

target.write(line1"\n",line2"\n",line3"\n")

print "lets read it!"

print text.read()

print "and finally we close it"
target.close()


