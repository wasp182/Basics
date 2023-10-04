parrot = "Indigo Blue"
print(parrot)
print(parrot[3])
# ans = i as indexing is from 0 as there is negative indexing also\
#print(parrot[-3])

str="We Win"

for i in range(1,len(str)+1):
    print(str[i-1])

##negative indexing with end of string starting from -1 and beginning start with index = 0

for i in range(1,len(str)+1):
    print(str[-i])
# SLicing with colon
print(parrot[0:6])
# substring in parrot but excluding last index
print(parrot[:6])
print(parrot[:])

# substring in negative indexes
print(parrot[-2:-4])
#prints all word
print(parrot[-4:-2])
#Bl printed

print(parrot[0:6:2])
## prints idg

number = "984;034,984:984,230,321"
separators = number[3::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])


