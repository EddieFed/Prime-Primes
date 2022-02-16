# https://vixra.org/pdf/1909.0461v1.pdf

from itertools import count
import numpy as np
from sympy import fibonacci

from sieve_eratosthenes import sieve

def fib_test(p: int) -> bool:
    res = False
    val = fibonacci(p) % p
    val2 = fibonacci(2*p) % (2*p)
    if val == 1 or val == p - 1:
        res = True
    if val2 == 1 or val2 == p - 1:
        res = res and True
    
    return res


# Tests
primes = []
with open("primes.txt") as file2:
    for line2 in file2:
        primes.append(int(line2))

cut_off = 100000

prime_count = 0
actually_prime_list = []
actually_composite_list = []
exceptions = 0

counter = 0
try:
    for n in range(1, cut_off):
        result = fib_test(n)
        if (result == False and n in primes):
            # print(f"Incorrectly identified {n} as composite (is prime)")
            actually_prime_list.append(n)
        elif (result == True and n not in primes):
            if (int(n/2) in primes):
                # print(f"Found 2p = 2({int(n/2)}) = {n}")
                exceptions += 1
            else:
                # print(f"Incorrectly identified {n} as prime (is composite)")
                actually_composite_list.append(n)
        elif result == True and n in primes:
            prime_count += 1

        counter += 1
except KeyboardInterrupt:
    print(f"Checked all numbers 1-{counter}:")
    print(f"    - Found a total of {prime_count} real primes")
    print(f"      (Correct total of primes is {np.count_nonzero(sieve(counter))})")
    print(f"    - Found {len(actually_prime_list)} number(s) to be composite but actually is prime!")
    print(f"        > {actually_prime_list}")
    print(f"    - Found {len(actually_composite_list)} number(s) to be prime but actually is composite!")
    print(f"        > {actually_composite_list}")
    print(f"    - Ignored a total of {exceptions} number(s) which are 2p and still follow the conjecture")

