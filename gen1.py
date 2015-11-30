def first_n(n):
	num = 1
	while num <= n:
		yield num
		num += 1

sum_of_first_10 = sum(first_n(10))
print('10',sum_of_first_10)
