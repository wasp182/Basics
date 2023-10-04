def fib():
    current = 0
    previous = 1
    while True:
        yield current
        current , previous = current + previous , current


fib = fib()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# iterator works on variable only ?
#