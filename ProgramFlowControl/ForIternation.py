# sample='blue indigo'
#
# for char in sample:
#     print('{}....'.format(char))
#############

# print(parrot[0:6:2])
# #prints idg
number = input('enter seris of number with seperators')
#separators = number[3::4]
# print(separators)
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])


separator=""
for char in number:
    if not char.isnumeric():
        separator=separator+char
print(separator)

values = "".join(char if char not in separator else " " for char in number).split()
print([int(val) for val in values])



