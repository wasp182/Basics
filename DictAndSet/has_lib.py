import hashlib

print(sorted(hashlib.algorithms_available))
print(sorted(hashlib.algorithms_guaranteed))

python_code='''for i whatever'''

original_hash=hashlib.sha256(python_code.encode('utf8'))

for bytes in python_code.encode('utf8'):
    print(bytes, chr(bytes))

print()
print("hash is {}".format(original_hash.hexdigest()))


