# crack password
# assume MD5 sum

import hashlib
from string import printable

# One lowercase letter only
answer = "e358efa489f58062f10dd7316b65649e"

for guess in printable:
	encoded_guess = guess.encode('utf-8')
	hashed = hashlib.md5(encoded_guess).hexdigest()
	if( hashed == answer ):
		print("password 1 is", guess)
		break

#------------------------------------------------

# Could be one or two letters or symbols

#sr
answer = "e22428ccf96cda9674a939c209ad1000"

#t
#answer = "e358efa489f58062f10dd7316b65649e"

for g0 in printable:
	for g1 in printable:
		guess = g0 + g1
		encoded_guess = guess.encode('utf-8')
		hashed = hashlib.md5(encoded_guess).hexdigest()
		if( hashed == answer ):
			print("password 2 is", guess)
			break

#------------------------------------------------
"""

# Could be up to eight letters or symbols
answer="fc45ed5aa04ed400b192101a11f5e580"

#for guess in printable:
#	encoded_guess = guess.encode('utf-8')
#	hashed = haslib.md5(encoded_guess).hexdigest()
#	if( hashed == answer ):
#		print(
"""
