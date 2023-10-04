letter = "qwertyuiop"
print(len(letter))

print(letter[-1:-11:-1])
print(letter[::-1])
##python idiom, start value must be greater than end value

print(letter[:-9:-1])
##last eight characters in reverse order
print(letter[2:5:1])
print(letter[-6:-9:-1])

#last 4 items
print(letter[-4:])

# last 4 items of list in reverse order
print(letter[:-5:-1])

#last item of list
print(letter[-1:])

# first item
print(letter[:1])
# this idiom can return first item without showing error on empty list i.e. index error wont be there if empty string

