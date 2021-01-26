import hashlib
import os
salt = os.urandom(256)
password = "Password123"

#Test Hash
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
print('Salt is: ', salt)

def hash_password(password, salt = os.urandom(256)):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
    print('Salt is: ', salt)
    return key
salt = key[:]
users_password = hash_password(str(input('Please enter your password: ')))
if users_password == key:
    print("True")
else:
    print("False") 