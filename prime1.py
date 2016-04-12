for i in range(2,100001):
	for factor in range(2,i):
		if(i % factor) == 0:
			#print ("found factor", factor)
			break
	else:
		print(i, "is prime")
