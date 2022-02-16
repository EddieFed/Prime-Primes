from random import randint

"""
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""

def mr(n: int, k: int):

    # First find n = (2^s)d
    s = 0
    d = n - 1

    # Divide d by 2 until it's odd
    while d % 2 == 0:
        s += 1
        d //= 2

    prob_prime_1 = False
    prob_prime_2 = False
    for _ in range(k):
        # Randomly decide a where a is in range (1, n-1)
        a = randint(1, n - 1)
        
        # This is an initial test
        if (pow(a, d, n) == 1):
            prob_prime_1 = True
            break

        # Check for all r within range [0, s)
        for r in range(s):
            # Second test, only needs to satisfy this once!
            if (pow(a, pow(2, r) * d, n) == n - 1):
                prob_prime_2 = True
                break

    return prob_prime_1 or prob_prime_2

print(mr(809218877666552262416755108038, 40))