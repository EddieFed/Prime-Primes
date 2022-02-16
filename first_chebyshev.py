# https://mathworld.wolfram.com/ChebyshevFunctions.html

import math
import matplotlib.pyplot as plt

w = 100

def cheb(primes: list[int], x: int):
    theda = 0
    for k in x:
        theda += math.log(primes[k-1])
    
    return theda

primes = []
with open("primes.txt") as file2:
    for line2 in file2:
        primes.append(int(line2))

y = [0]
for n in range(1, w):
    y.append(cheb(primes, n))

X = range(w)
plt.plot(X, y, color='r')
plt.plot(X, X, color="g")
plt.show()