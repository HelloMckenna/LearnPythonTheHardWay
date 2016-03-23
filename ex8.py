
# Here the variable is filled with format characters, I've changed is so that  it shows the difference between using
#  string formatters %s and representations or raw formatter %r
formatter = "%s %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    'I had this thing.',
    "That you could type right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print '" STUFF "'

# Note difference in using string and raw format characters. Python takes the most computationally efficent route
# when not using the raw %r format character, it will only print "" when it is done through ' " " '