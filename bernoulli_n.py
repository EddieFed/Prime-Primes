#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import ROUND_HALF_EVEN, Decimal
from fractions import Fraction as Fr
from math import ceil, factorial, floor, gcd
from numbers import Rational

import sympy

from sieve_eratosthenes import sieve

"""
bernoulli_num(n) generates the first n bernoulli numbers and stiores only the even bernoulli number
numerators (B(k) where k = 2n) in a file names bernoulli.txt. This script is a slightly modified version of the
code found at https://rosettacode.org/wiki/Bernoulli_numbers#Python . Personally, I didn't
have any use for the denominator of the bernoulli numbers so I simply ignore them. This is much
more optimal for space, however, the algorithm is still stunted in terms of speed since its practically exponential,
taking nearly 9 hours to generate B(0) -> B(10,000) on an intel i7-6700k
"""

n = 1000    # Number of bernoulli numbers to generate.
            #The numerators wil be written to bernoulli.txt

def bernoulli_generator():
    A, m = [], 0
    while True:
        A.append(Fr(1, m+1))
        for j in range(m, 0, -1):
            A[j-1] = j*(A[j-1] - A[j])
        yield A[0] # (which is Bm)
        m += 1

def bernoulli_num(n: int):
    bn = [ix for ix in zip(range(n), bernoulli_generator())]
    bn = [(i, b) for i,b in bn if b]

    with open("bernoulli.txt", "w+") as file:
        index = 0
        for i, b in bn:
            # print('B(%2i) = %*i/%i' % (i, width, b.numerator, b.denominator))
            if (index > 1):
                file.write("%s\n" % str(b.numerator))
            index += 1
    
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286')
def bernoulli_pi(n: int) -> int:
    """
    https://vixra.org/pdf/1409.0083v1.pdf
    """

    K = (2*factorial(n))/((2*pi)**n)

    # Build prime list!
    index = 0
    primes = []
    for p_bool in sieve(n+1):
        if p_bool:
            primes.append(index)
        index += 1

    d = 1
    for p in primes:
        if n%(p-1)==0:
            d *= p

    N = ceil((K*d)**(1.0/(n-1)))

    z = 1
    for p in primes:
        if p <= N:
            z *= 1/(1-1/((p)**n))

    a = Decimal((-1)**(n/2+1)*(d*K*z))
    a.to_integral_exact(rounding=ROUND_HALF_EVEN)
    if a == 0:
        a = (-1)**(n/2+1) 
    print(a)    # Print numerator
    # print(d)    # Print denominator
    # return a/d

bernoulli_pi(2)