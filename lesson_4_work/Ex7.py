import hashlib
password = "nastya"
hashPassword = hashlib.sha256(password.encode()).hexdigest()
print(hashPassword)