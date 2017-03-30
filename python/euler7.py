"""
euler7.py

Evan Greene
2016/12/02

Solves problem 7 on project euler

By listing the first six prime numbers, 2, 3, 5, 7, 11, 13, we can see that the
sixth prime number is 13.

What is the 10 001st prime number?
"""

def main():
    # n = 6
    n = 10001
    primes = [None] * n
    primes[0] = 2

    for i in range(len(primes) - 1):
        j = primes[i] + 1
        while True:
            primeflag = True
            for p in primes:
                if p is None:
                    continue
                if j % p == 0:
                    primeflag = False
                    break
            if primeflag:
                primes[i+1] = j
                break
            else:
                j+= 1

    print primes[-1]

main()
