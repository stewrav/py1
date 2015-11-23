# sroot2.py

debug = 0
dp = 5  # number of decimal places to use

# Derive tolerance from dp
# as tolerance = 1x10e(-dp)
tolerance = 10 ** (-1 * dp)

# Find square roots of the following numbers
for i in range(2,101):

	print("Number ==", i)

	# Start with some initial guesses
	lo_guess = 0
	hi_guess = i
	
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

		# If we are within tolerance
		if(test - tolerance < i < test + tolerance):
			# then break out of the loop for this number
			break
			
		# If the test shows that our guess is too low
		elif(test < i):
			# then set the lower boundary to be the current guess
			if debug: print("Too low")
			lo_guess = guess
			
		# If the test shows that our guess is too high
		else:
			# then set the upper boundary to be the current guess
			if debug: print("Too high")
			hi_guess = guess
			
		# Show a blank line if we are in debug mode
		if debug: print()

	# Show the result for this number
	print("square root ==", round(guess,dp), "\n")
