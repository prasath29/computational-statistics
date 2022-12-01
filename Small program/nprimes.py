# finding the first n prime numbers
n = 15

i = 2
primes = []

while n:
    for prime in primes:
        if i%prime == 0:
            break
    else:
        primes.append(i)
        n -= 1

    i += 1

print(primes)
