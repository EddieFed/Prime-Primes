#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import time

import numpy as np

"""
sieve() is optimized to use as little space as possible when running.
Generally in python, an Integer takes 28 bytes of memory, so working in large quantities
is unreasonable for arrays of size 1 billion. However, this uses numpy ndarrays which can
use the ctype bool taking a measly 1 byte per value. This is more time consuming to iterator
over when writing to a file, but much less memory intense allowing for much larger quantities
of primes to be generated without nearly as much memory overhead
"""

def sieve(n: int) -> np.ndarray:
    """
    Returns a boolean array where the index is the number
    and the boolean at the index determines if that index value is prime

    Parameters
    ----------
    n : int
        Upper limit to generate primes

    Returns
    -------
    out : ndarray
        Array determining primes of the array indicies
    """

    bools = np.full(n + 1, True)
    bools[0] = False
    bools[1] = False
    i = 2   # Start at 2 since 0 and 1 are not primes

    while (i * i <= n):
        # If prime[i] is not changed, then it is a prime
        if (bools[i]):
            # Update all multiples of i as False
            for j in range(i ** 2, n + 1, i):
                bools[j] = False
        # Check next number
        i += 1

    return bools


if __name__=='__main__':
    start = time.time()
    output_file = "primes.txt"

    n = 100000000           # n can be changed to anything for this project,
    primebool = sieve(n)    # we're mainly working with primes up to the limit 100,000,000
    mid = time.time()

    with open("primes.txt", "w+") as file:
        file.seek(0)    # Begins at start of file
        for i in range(n + 1):
            if (primebool[i]):
                file.write("%s\n" % i)
        file.truncate() # Wipes remaining file clean

    # Total time taken
    end = time.time()
    print(f"Generated a total of {np.count_nonzero(primebool)} primes!")
    print(f"-> Sieve runtime was {math.floor(mid-start)} seconds")
    print(f"-> Total runtime was {math.floor(end-start)} seconds")