def factorial(n : int) -> int :
    '''
    performs factorial operation
    :param n: input integer
    :return: factorial value of input
    '''
    if n == 0:
        return 1
    else:
        answer = n*factorial(n-1)
    return answer


for i in range(36):
    print(factorial(i))
