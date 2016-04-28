print "please entre the file you wish to read"

txt = raw_input("> ")

txt_file = open(txt)

print txt_file.read()