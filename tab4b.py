#tables test

from random import randint

import time

tables = [2,3,6]
tables2 = range(1,13)

numcor = 0

nq=5

start_time = time.monotonic()

max_attempts = 2


for question_num in range (0,nq):

	x_index=randint(0,len(tables)-1)
	y_index=randint(0,len(tables2)-1)
	x=tables[x_index]
	y=tables2[y_index]
	
	attempts = 0
	
	while attempts < max_attempts:
		attempts = attempts+1
		

		print ("what is",x,"times",y,"?")

	#work out the answer!
		try:
			ans = int(input())
			break
		except ValueError:
			print ("that answer wasn't sensible")
			ans=0
			
		
		
	if ans == x*y:
		print("you were correct!")
		numcor = numcor + 1
	
	else:
		print("you were wrong! The answer was",x*y)
	
end_time = time.monotonic()

time_taken = int(0.5 + end_time - start_time)
	
print ("you got",numcor,"out of",nq, "You did it in", time_taken,"seconds!")

if numcor == nq:
	print ("You got all the questions correct! Well done!")
	
