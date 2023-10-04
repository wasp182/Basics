entries = [1,2,3,4,5]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print()

entries_zero = [1,2,3,0,6]
print("all: {}".format(all(entries_zero)))
print("any: {}".format(any(entries_zero)))

name =""
if name:
    print("hello {}".format(name))
else:
    print("bye")

print()
# weird behaviour of all()
entry =[]
print(all(entry))
# this evaluates to true as we need to evaluate entry to false or boolean value
# in order to get consistent result
# all by itself will return true
res =  (bool(entry) and all(entry))
print(res)
