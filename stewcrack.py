# crack password
# assume MD5 sum

import hashlib
from string import ascii_lowercase, printable

# One lowercase letter only
answer = "e358efa489f58062f10dd7316b65649e"

for guess in ascii_lowercase:
	encoded_guess = guess.encode('utf-8')
	hashed = hashlib.md5(encoded_guess).hexdigest()
	if( hashed == answer ):
		print("password is", guess)
		break


# Could be one or two letters or symbols
answer = "e22428ccf96cda9674a939c209ad1000"

for guess in printable:
	encoded_guess = guess.encode('utf-8')
	hashed = hashlib.md5(encoded_guess).hexdigest()
	if( hashed == answer ):
		print("password is", guess)
		break

for g0 in printable:
	for g1 in printable:
		guess = g0 + g1
		encoded_guess = guess.encode('utf-8')
		hashed = hashlib.md5(encoded_guess).hexdigest()
		if( hashed == answer ):
			print("password is", guess)
			break
