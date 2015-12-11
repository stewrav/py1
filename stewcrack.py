# crack password
# assume MD5 sum

import hashlib
from string import ascii_lowercase

answer = "e358efa489f58062f10dd7316b65649e"

for guess in ascii_lowercase:
	encoded_guess = guess.encode('utf-8')
	hashed = hashlib.md5(encoded_guess).hexdigest()
	if( hashed == answer):
		print("password is", guess)
