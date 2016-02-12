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

def guess_correct(g):
	encoded_guess = g.encode('utf-8')
	hashed = hashlib.md5(encoded_guess).hexdigest()
	if( hashed == answer ):
		print("password is", g)
		return True
	else:
		return False

for g1 in printable:
	for g2 in printable:
		if guess_correct(g1 + g2):
			break

#------------------------------------------------

#"""

# Could be up to eight letters or symbols
answer="fc45ed5aa04ed400b192101a11f5e580"

# 1
for g1 in printable:
	if guess_correct(g1):
		quit()

# 2
for g1 in printable:
	for g2 in printable:
		if guess_correct(g1+g2):
			quit()

# 3
for g1 in printable:
	for g2 in printable:
		for g3 in printable:
			if guess_correct(g1+g2+g3):
				quit()

# 4
for g1 in printable:
	for g2 in printable:
		for g3 in printable:
			for g4 in printable:
				if guess_correct(g1+g2+g3+g4):
					quit()

# 5
for g1 in printable:
	for g2 in printable:
		for g3 in printable:
			for g4 in printable:
				for g5 in printable:
					if guess_correct(g1+g2+g3+g4+g5):
						quit()

# 6
for g1 in printable:
	for g2 in printable:
		for g3 in printable:
			for g4 in printable:
				for g5 in printable:
					for g6 in printable:
						if guess_correct(g1+g2+g3+g4+g5+g6):
							quit()

# 7
for g1 in printable:
	for g2 in printable:
		for g3 in printable:
			for g4 in printable:
				for g5 in printable:
					for g6 in printable:
						for g7 in printable:
							if guess_correct(g1+g2+g3+g4+g5+g6+g7):
								quit()

#8
for g1 in printable:
	for g2 in printable:
		for g3 in printable:
			for g4 in printable:
				for g5 in printable:
					for g6 in printable:
						for g7 in printable:
							for g8 in printable:
								if guess_correct(g1+g2+g3+g4+g5+g6+g7+g8):
									quit()

#"""
