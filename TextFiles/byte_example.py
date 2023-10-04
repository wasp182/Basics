eq = bytes((112,123,100,99,22))
# eq= b'\x0c\x17"8\xde'
rew = bytes()
print(eq)

for b in eq:
    print(b,end=", ")

print()
print(eq.decode("utf-8"))
