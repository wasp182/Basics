# i=0
# while i<10:
#     print(i)
#     i+=1
#

# available_options = ['north','south','east','west']
# chosen_exit=""
#
# while chosen_exit not in available_options:
#     chosen_exit=input('enter exit option').casefold()
#
# available_options = ['north','south','east','west']
# chosen_exit=""
# while chosen_exit not in available_options:
#     chosen_exit=input('enter exit option').casefold()
#     if chosen_exit.casefold()=='quit':
#         print('game over')
#         break
#
#
# i=0
# while (i<100):
#     print(i)
#     if(i%11==0 and i!=0):
#         break
#     i=i+7

i=0
while (i<=20):
    if(i%3==0 or i%5==0):
        i+=1
        continue
    else: print(i)
    i+=1