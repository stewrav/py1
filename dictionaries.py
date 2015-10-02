dad = 'Stewart'
fam = { 'man':dad, 'woman':'mum', 'youngest boy':'ollie', 'girl':'berry','eldest boy':'eddie' }

# To just list the keys:
#for item in fam:
#	print(item)
#print('')

# Iterate through each key in the dictionary,
# displaying the key and its value
for key,value in fam.items():
	print ("it's the", key, "and it's name is", value)
