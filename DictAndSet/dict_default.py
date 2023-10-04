from contents import pantry

print(pantry)
print(pantry.setdefault("chicken",0))
print(pantry.get("Beans",0))

for key,values in sorted(pantry.items()):
    print(key,values)

