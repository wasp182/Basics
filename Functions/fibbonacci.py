def fibonacci(n):
    '''
    returns nth Fibonacci number
    :param n: positive 'int'
    :return: fibonacci number
    '''
    if 0<=n<=1:
        return n
    n1,n2=0,1
    result=None
    for i in range(1,n):
        result=n1+n2
        n1=n2
        n2=result
    return result
# in case negative value is passed , result will be thrown without being
# bound to value


for index in range(36):
    print(fibonacci(index))