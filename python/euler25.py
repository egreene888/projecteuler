"""
euler25.py

Solves problem 25 in project euler

Problem Statement:

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_(n-1) + F_(n-2), where F_1 = 1 and F_2 = 1

Hence, the first 12 terms will be 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.

The 12th term, 144, is the first fibonnacci number to contain 3 digits.

What is the index of the first fibonnacci number to contain 1000 digits.
"""

def main():
    Fn = 2
    Fnminus1 = 1
    Fnminus2 = 1
    n = 3

    while Fn < 1e999:
        # while Fn < 1e2: # test case
        Fnminus2 = Fnminus1
        Fnminus1 = Fn
        Fn = Fnminus1 + Fnminus2

        n += 1

    print 'The first fibonacci number with more than 1000 digits is number {}'.format(n)

main()
