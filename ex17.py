from sys import argv
from os.path import exists

script, from_file, to_file = argv

print " Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file); indata = in_file.read()

print "This input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()


"""
Study Drills

1 Tidy up the script

2 The whole script could be one line long if ; is used between each line instean of a return.

3. ???

4. Had to write out_file.close() to close the file after opening it. Its only good house keeping!

5. Read about Python's import statement...

"""