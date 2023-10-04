name = input('please enter your name')
age = int(input('please enter your age {0}'.format(name)))
# make sure to give only interger else it will crash , exception handling required
print(age)
#
# if age>= 18:
#     print('you can vote')
#     print('money money')
# else:
#     print('bro dont vote , shit is illegal')

# elif is concludeed if 'if' statement is not fullfilled
if age>= 18:
    print('you can vote')
elif age == 18:
    print("baby yoda up in here")
else:
    print('bro dont vote , shit is illegal')



