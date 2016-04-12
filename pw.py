# Store password

# Need salt
# Need slowness

from passlib import pbkdf2_sha256

myhash = pbkdf2_sha256.encrypt("open sesame", rounds=1003, salt_size=20)
print("myhash ==", myhash)
