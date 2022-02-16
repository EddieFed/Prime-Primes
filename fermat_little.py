from random import randint

"""
https://en.wikipedia.org/wiki/Fermat_primality_test
"""

def little_theorem(n: int, k: int) -> bool:

    # These are easily determined, no need for the flt
    if (n < 2):
        return False
    elif (n == 2 or n == 3):
        return True
    elif (n % 2 == 0):
        return False

    # we now have k, m such that m is an odd integer

    for _ in range(k):

        a = randint(2, n - 2)
        
        if (pow(a, n - 1, n) != 1):
            return False
    
    # if all iterations were completed without throwing False, then n is probably prime
    return True

print(little_theorem(809218877666552262416755108037, 40))