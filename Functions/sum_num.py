def sum_num(*a: float) -> float:
    '''
    returns sum of  input no
    :param a: var # of numbers to be summed
    :return: sum of input numbers
    '''
    result = 0
    for i in a:
            result += i
    return result


print(sum_num(1, 2, 4))
f1='2.34'
print(float(f1))

