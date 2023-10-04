st1="hello"
print(st1*3)
#print(st1*3+2)
#error because of mismatching class types , str is tring type and 2 is int

print("ello" in st1)
#true return
print("llo" in st1)
print("day" in st1)

age = 24
print('my age is '+ str(age))

## alternate way to print strings and integer is replacement and format method , {N} - this is the replacement field
print("my age is {0}".format(age))
print("my birthday is on {0} {1} {2}".format(18,"June",1995))
date = [18,"June",1996]
print("my birthday is on {0} {1} {2} i am older than {0}".format(18,"June",1995))
