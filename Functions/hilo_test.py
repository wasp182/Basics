LOW = 1
HIGH = 1000

# print('think of no between {0} and {1}'.format(low,high))

def binary_guess(answer,low,high):
    guesses = 1
    while low!=high:
        print('\t guessing in range of {} ato {}'.format(low,high))
        guess = low + (high - low)//2
        # user_input= input('enter H or L if the number is higher or lower '
        #                   'than {0}.If guess is correct type C'.format(guess)).casefold()
        if guess<answer:
            low = guess + 1
        elif guess>answer:
            high = guess - 1
        elif guess==answer:
            return guesses
        else:
            print('invalid input. try again')
            continue
        guesses+=1
    else: print('the number is {}, guessed in {} tries'.format(guess,tries))
