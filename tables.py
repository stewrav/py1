# Tables Test

# Import randint function
from random import randint

# Import monotonic function
import time

# Numbers for left-hand side
table1 = [ 2, 3, 6 ]

# Numbers for right-hand side
table2 = range( 1, 13 )

# Say how many questions there will be
numq = 3

# Count how many correct
numcorrect = 0

# Maximum number of silly guesses
max_attempts = 2

# Note the time
start_time = time.monotonic()

# Loop through the questions
for question_number in range(1,numq+1):

	# Give me a random index between 0 (start) and len-1 (end)
	x_index = randint( 0, len(table1)-1 )
	y_index = randint( 0, len(table2)-1 )

	# With the random index choose a random element from the list of numbers
	x = table1[x_index]
	y = table2[y_index]

	# Work out the answer!
	z = x * y
	#print( "z ==", z )

	attempts = 0
	while attempts < max_attempts:
	
		# Increment the attempt counter
		attempts += 1

		# Ask the question
		print( "(", question_number, ") What is ", x, " times ", y, "?", sep="" )
		answer_string = input()

		# Try to turn the answer into a number
		try:
			answer = int( answer_string )
			break

		except ValueError:
			print( "Your answer (", answer_string, ") isn't sensible\n" )
			answer = 0
	
	# Check the answer
	if answer == z:
		print("Correct!")
		numcorrect += 1
	else:
		print("Wrong")
	print("\n")

# Note the time
end_time = time.monotonic()

if (numcorrect == numq):
	print("Perfect!")

print("You scored", numcorrect, "out of", numq, "(in", int(0.5 + end_time - start_time), "seconds)")
