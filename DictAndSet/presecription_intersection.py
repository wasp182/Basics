from prime_squares_generator import primes_generator,squares_generator

odds= set(range(1,50,2))
evens = set(range(0,50,2))

odd_sqaures = odds.intersection(squares_generator(50))
even_squares = evens.intersection(squares_generator(50))

print(f"Odd sqaures : {odd_sqaures}")
print(f"Even sqaures : {even_squares}")

odd_primes=odds.intersection(primes_generator(50))
print(odd_primes, sep='\t')
