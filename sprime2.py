def get_primes():
	candidate = 2
	found = []
	while True:
		if all(candidate % prime != 0 for prime in found):
			yield candidate
			found.append(candidate)
		candidate += 1

primes = get_primes()

for _, prime in zip(range(9592), primes):
	print(prime)
