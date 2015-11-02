#tables test

from random import randint


tables = [2,3,6]
tables2 = range(1,13)

numcor = 0

nq=5

for question_num in range (0,nq):

	x_index=randint(0,len(tables)-1)
	y_index=randint(0,len(tables2)-1)
	x=tables[x_index]
	y=tables2[y_index]


	print ("what is",x,"times",y,"?")

	#work out the answer!

	ans = int(input())
	if ans == x*y:
		print("you were correct!")
		numcor = numcor + 1
	
	else:
		print("you were wrong! The answer was",x*y)
	

print ("you got",numcor,"out of",nq)

if numcor == nq:
	print ("You got all the questions correct! Well done!")
	
