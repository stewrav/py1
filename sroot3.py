# sroot2.py
import math

dp = 5  # number of decimal places to use

# Derive tolerance from dp
# as tolerance = 1x10e(-dp)
tolerance = 10 ** (-1 * dp)

# Find square roots of the following numbers
for i in range(2,100001):

	print("Number ==", i)
	print("square root ==", round(math.sqrt(i),dp), "\n")
