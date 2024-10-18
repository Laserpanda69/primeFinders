import math
def check_prime(prime_candidate: int) -> bool:
    if prime_candidate == 1:
        return False

    primes = find_primes(n = prime_candidate)

    return primes[-1] == prime_candidate


def find_primes(n):
    primes = []
    # this generates all primes less than sqrt(prime_candidate)
    for head in range(2, n+1):

        if not primes:
            # not primes => no primes found => no way to construct numbers from existing primes => number must be prime
            primes.append(head)
            continue


        head_is_prime = True
        for prime in primes:
            # If head/ some prime is 0 then head is a multipul of a prime => is not prime
            head_is_prime = head % prime != 0
            # We can exit as soon as we find out a number is not prime
            if not head_is_prime:
                break

        
        # Due to exiting early, at this stage head must be a prime number
        if head_is_prime:
             primes.append(head) 

    return primes
        

print(check_prime(20))

