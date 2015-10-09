# Tables Test

# Import randint function
from random import randint

# Numbers for left-hand side
table1 = [ 2, 3, 6 ]

# Numbers for right-hand side
table2 = range( 1, 13 )

# Say how many questions there will be
numq = 3

# Loop through the questions
for question_number in range(0,numq):

	# Give me a random index between 0 (start) and len-1 (end)
	x_index = randint( 0, len(table1)-1 )
	y_index = randint( 0, len(table2)-1 )

	# With the random index choose a random element from the list of numbers
	x = table1[x_index]
	y = table2[y_index]

	# Work out the answer!
	z = x * y
	#print( "z ==", z )

	# Ask the question
	print( "What is", x, "times", y, "?" )
	answer_string = input()

	# Turn the answer into a number
	answer = int( answer_string )
	#print( "answer ==", answer )

	# Check the answer
	if answer == z:
		print("Correct!")
	else:
		print("Wrong")

