#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

"""
This is a standalone script not meant to be called independently. This script reads
in all primes generated from sieve() and all bernoulli number numerators from
bernoulli_num(). It will spit out a new text file named regular.txt which contains
only regular prime numbers.

Regular Primes:
    Def => Prime numbers p which do not divide the numerator of any bernoulli number B(k)
    for all k where k = 2n and k <= p-3.

    For more info see: https://oeis.org/A007703
"""

# If neither file exists, abort!
if (not os.path.exists("bernoulli.txt") or not os.path.exists("primes.txt")):
    print("Please ensure that bernoulli.txt and primes.txt are in the root directory!")
    exit()

bernoulli_n = []
with open("bernoulli.txt") as file:
    for line in file:
        bernoulli_n.append(int(line))

primes = []
with open("primes.txt") as file2:
    for line2 in file2:
        primes.append(int(line2))

# Determine the largest prime which we are allowed to check!
p_3 = len(bernoulli_n)*2 + 3

regular_primes = []
for p in primes:
    if (p <= p_3):
        if (p-3 >= 0):  # This will exlude 2 since B(2-3) is not a valid bernoulli number
            is_reg = True
            # print(f"Checking if {p} is regular")

            # Check the divisibility of all even bernoulli numbers less than p-3
            index = 2 
            for b in bernoulli_n:

                # Only check B(k) for 2, 4, 6, ..., p-3
                if (index > p-3):
                    break

                # If p divides B(k), than it is not a regular prime
                if (b % p == 0):
                    is_reg = False
                    break

                # This is just to keep track of p < p-3
                index += 2
        else:
            is_reg = False

        if (is_reg):
            # print(f"{p} is regular")
            regular_primes.append(p)

    else:
        break

# Dump it all to a file!
with open("reg.txt", "w+") as file:
    for reg in regular_primes:
            file.write("%s\n" % str(reg))


# Below is the method for checking regularity from https://oeis.org/A007703
#
# from sympy import prime, isprime, bernoulli
#
# def ok(n):
#     print(f"Testing {n}")
#     for k in range(2, n - 2, 2):
#
#         if bernoulli(k).as_numer_denom()[0] % n == 0:
#
#             return 0
#
#     return isprime(n)
#
# reg = [n for n in range(3, 10000) if ok(n)]
#
# with open("reg2.txt", "w+") as file:
#     for r in reg:
#             file.write("%s\n" % str(r))