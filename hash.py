import hashlib

def show_pw_and_hash(secret):
	print("secret ==", secret)
	encoded_secret = secret.encode('utf-8')
	hashed = hashlib.md5(encoded_secret).hexdigest()
	print("hashed ==", hashed, "\n")

	
show_pw_and_hash("t")
show_pw_and_hash("sr")
show_pw_and_hash("abCd3Fgh")
show_pw_and_hash("S8")
