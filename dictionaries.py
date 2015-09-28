dad = 'Stewart'
fam = { 'man':dad, 'woman':'mum', 'boy':'ollie' }

# To just list the keys:
#for item in fam:
#	print(item)
#print('')

# Iterate through each key in the dictionary,
# displaying the key and its value
for key,value in fam.items():
	print( 'The', key, 'is', value )
