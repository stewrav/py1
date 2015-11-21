# write to config file

config_file = ".test"
blah = "hello world"

#----------------------------

f = open(config_file, 'w')
#print("f ==", f)
f.write(blah)
f.close()

#----------------------------

g = open(config_file, 'r')
for line in g:
	print("line ==", line, end='')

g.close()
