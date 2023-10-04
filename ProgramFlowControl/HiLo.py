low = 1
high = 1000

print('think of no between {0} and {1}'.format(low,high))
guess = 1
tries = 0

while low!=high:
    print('\t guessing in range of {} ato {}'.format(low,high))
    guess = low + (high - low)//2
    user_input= input('enter H or L if the number is higher or lower '
                      'than {0}.If guess is correct type C'.format(guess)).casefold()
    if user_input == "h":
        low = guess + 1
    elif user_input == "l":
        high = guess - 1
    elif user_input == "c":
        break
    else:
        print('invalid input. try again')
        continue
    tries+=1
else: print('the number is {}, guessed in {} tries'.format(guess,tries))
