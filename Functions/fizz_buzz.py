def fizz_buzz(n: int)-> str:
    '''
    Tests input n for divisibility by 3 and 5
    :param n: `int` to test
    :return: returns 'fizz' if n is divisible by 3 , 'buzz' if n is divisible
    by 5 and 'fizz buzz' if divisible by both
    '''
    if n%3==0 and n%5==0 :
        return "fizz buzz"
    elif n%3==0:
        return "fizz"
    elif n%5==0:
        return "buzz"
    else:
        return str(n)


index = 1
while True:
    if index<100:
        print(fizz_buzz(index))
        index +=1
        guess=fizz_buzz(index)
        human_guess=input(': ')
        if human_guess==guess:
            index+=1
            continue
        else:
            print('incorrect guess, you lose')
            break
    else:
        print('game over')
        break




