"""
The sum of primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all primes below two million.

This solution uses a lot of memory, but hopefully runs quickly.
It doesn't run quickly.

Works... kinda.
"""
import math

def main():
    sumofprimes = 0
    primes = []
    for i in range(2, 2000000):
        primeflag = True
        for prime in primes:
            if prime > math.sqrt(i):
                break
            if i % prime == 0:
                primeflag = False
                break
        if primeflag:
            primes.append(i)
            sumofprimes += i
            # print i
    print sumofprimes

main()
