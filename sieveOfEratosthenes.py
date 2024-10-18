import math







def check_prime(prime_candidate):
    sieve = [[n, True] for n in range(1, prime_candidate+1)]
    VALUE_INDEX = 0
    PRIME_INDEX = 1
    sieve[0][PRIME_INDEX] = False
    primes = []

    # Generates all primes needed to check if candidate is prime
    radical_candidate = math.sqrt(prime_candidate)
    for i in range(1, radical_candidate):
        if sieve[i][PRIME_INDEX]:
            primes.append(sieve[i][VALUE_INDEX])
            # Sets all the multipuls of i (which is prime) to be not prime
            for j in range(i, len(sieve), i):
                sieve[j][PRIME_INDEX] = False






