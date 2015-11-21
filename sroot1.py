# sroot1.py

for i in range(1,101):
	for j in range(1,i):
		if(j ** 2) == i:
			print("The square root of", i, "is", j)
			break
