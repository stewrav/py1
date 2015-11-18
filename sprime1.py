# Prime numbers

# Test these numbers
for i in range(2,100):

	# Test factors
	for j in range(2,i):

		# If divided with no remainder
		if i % j == 0:

			# then skip to next number
			break
	# If got to here then did not break
	else:
		# So we had no factors
		print(i)

