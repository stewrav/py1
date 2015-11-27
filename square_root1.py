sq_root_range = range(2,100001)

for num in sq_root_range:
	print()
	print("The number is",num)
	lowest_guess = 0
	highest_guess = num
	while True:
		mid_point = lowest_guess + (highest_guess - lowest_guess)/2
		#print (mid_point)
		test = mid_point **2
		if round(test,10) == round(num,5):
			print("weel done the square root of",num, "is",round(mid_point,5))
			break
		elif test<num:
			lowest_guess =  mid_point
		else:
			highest_guess = mid_point
		
		
		