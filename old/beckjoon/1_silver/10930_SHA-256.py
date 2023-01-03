import hashlib

k = input()

result = hashlib.sha256(k.encode())
print(result.hexdigest())