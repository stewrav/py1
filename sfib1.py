# Fibonacci numbers in Python 3

def all_fib():
	
	a, b = 0, 1
	yield a
	yield b
	
	while True:
		a, b = b, a+b
		yield b

def part_fib( start, end ):
	
	for curr in all_fib():
		if curr > end:    return
		if curr >= start: yield curr

for i in part_fib( 1, 20 ):
	print( i )
