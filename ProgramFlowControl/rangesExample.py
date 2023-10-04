# for i in range(1,10):
#     print('i is now {}'.format(i))
#
# for i in range(1,10,2):
#     print('i is now {}'.format(i))
#
# for i in range(10,0,-2):
#     print('i is now {}'.format(i))
#
# age=3434
# if age in range(16,66):
#     print('ok')
# else: print('nope')

shoplist =['pasta','milk','spam']

for item in shoplist:
    if item=='spam':
        continue
    print('buy {}'.format(item))
