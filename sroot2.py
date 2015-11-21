# sroot2.py

debug = 0
tolerance = 0.00001
rounding = 5

for i in range(2,101):

	print("Number ==", i)

	# Start with some initial guesses
	lo_guess = 0
	hi_guess = i
	guess = (lo_guess + hi_guess)/2
	test = guess ** 2

	# Keep looping until we are within tolerance
	while True:

		# Make the guess and test it
		guess = (lo_guess + hi_guess)/2
		test = guess ** 2

		if debug: print("i ==", i)
		if debug: print("lo_guess ==", lo_guess)
		if debug: print("hi_guess ==", hi_guess)
		if debug: print("guess ==", guess)
		if debug: print("test ==", test)

		if(test+tolerance > i and test-tolerance < i):
			# We are within tolerance
			break
		elif(test < i):
			if debug: print("Too low")
			lo_guess = guess
		else:
			if debug: print("Too high")
			hi_guess = guess
		if debug: print()

	print("square root ==", round(guess,rounding), "\n")

