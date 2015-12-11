fibrange = range(1,11)

fibonacci1 = 1

fibonacci2 = 0

for num in fibrange:
	
	added_fib1 = (fibonacci1 + fibonacci2)
	print (added_fib1,", ")
	added_fib2 = (added_fib1 + fibonacci1)
	print (added_fib2,", ")
	added_fib3 = (added_fib1 + added_fib2)
	print (added_fib3,",")
	fibonacci1 = added_fib3
	fibonacci2 = added_fib2
	
	
	
	
	