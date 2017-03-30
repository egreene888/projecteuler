"""
The sum of primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all primes below two million.

This solution uses a lot of memory, but hopefully runs quickly.
It doesn't run quickly.

Works... kinda.
"""

def main():
    # n = 10
    n = 2000000

    answer = 0

    L = range(2, n)

    for i in range(len(L)):
        if L[i] == 0:
            continue
        for j in range(len(L)):
            if L[j] == 0 or L[j] == L[i]:
                continue
            if L[j] % L[i] == 0:
                L[j] = 0
        
    answer = sum(L)



    print 'The answer is %d' %(answer)


main()
