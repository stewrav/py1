import hashlib

secret = "t"
encoded_secret = secret.encode('utf-8')
hashed = hashlib.md5(encoded_secret).hexdigest()

print("secret ==", secret)
print("hashed ==", hashed)
