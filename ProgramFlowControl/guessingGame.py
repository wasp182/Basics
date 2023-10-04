import random
highest = 10
answer = random.randint(1,highest)
print(answer)
tries=int(input('no of time you want to play'))
guess=int(input('please guess no bw 1 and 10'))
#inefficient code
# if guess > answer:
#     print('guess lower')
#     guess = int(input('please guess again'))
#     if guess==answer:
#         print('done')
#     elif guess > answer:
#         print('guess lower again')
#     else: print('too low, better luck next time')
# elif guess< answer:
#     print('guess higher')
#     guess=int(input('please guess again'))
#     if guess==answer:
#         print('done')
#     elif guess < answer:
#         print('guess higher again')
#     else: print('too high, better luck next time')
# else:
#     print('you got it')

## 2 tries only tells if you got it, better
# if guess!= answer:
#     if guess > answer:
#         print('guess lower')
#     else: print('guess higher')
#     guess = int(input('please guess again'))
#     if guess!=answer:
#         print('still not right')
#     else:print('got it second time')
# else: print('got it right')
#
## 2 tries but also tells if you got it too high or low
# if guess!=answer:
#     if guess>answer:
#         print('too high')
#     else:print('too low')
#     guess=int(input('guess again'))
#     if guess==answer:
#         print('done')
#     elif guess>answer:
#         print('too high')
#     else: print('too low')
# else:print('you got it')

# checks no of tries and returns if successful or failed in n tries with final state of guess
t="start"
i=1
while(guess!=answer and i<tries):
    if guess> answer:
        print('too high')
        t='high'
    else:
        print('too low')
        t='low'
    if tries>1:
        guess=int(input('Take another guess or press 0 to escape'))
        if guess==0:
            break
    i+=1

if guess==answer:
    print('you got it')
elif guess!=0:
    print('no cigar in {0} tries , too {temp}. Correct value was {a}'.format(tries,temp=t,a=answer))
else: print('game over')

#TODO : remove the print answer