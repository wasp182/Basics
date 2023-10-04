data="asfkabj"
for t in enumerate(data):
    print(t)
    print(type(t))

# index,item=(0,'a')
# index=1
# this assignment/change is allowed as index is not a tuple but an unpacking variable
# print(index,item)

# Use above unpacking variables to play with tuples value
for t in enumerate(data):
    index,character= t
    print(index,type(index))
    print(character,type(character))

