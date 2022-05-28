import hashlib

password = input("Give me the password: ")
hash_password = password.encode()
x = hashlib.sha256(hash_password)
hashed = x.hexdigest()
print(hashed)
