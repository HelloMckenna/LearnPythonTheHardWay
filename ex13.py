# From the system, import argument varibles..

from sys import argv

# The argument varuables are called:

script, first, second, third = argv

# In order to call these variables, the must be named when the variable is being called. e.g. in powershell: ""py ex13.py first 2nd 3rd""

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third