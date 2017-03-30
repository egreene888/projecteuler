"""
euler23.py

Solves problem 23 in project euler.

Problem statement:
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater than
28123 can be written as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

def is_abundant(n):
    factors = 1 # 1 is a factor for every number.
    limit = n/2
    i = 2
    while i < limit:
        if n % i == 0:
            factors += i + n/i
            limit = n/i
        i += 1
        # print factors, limit, i
    if factors > n:
        return True
    else:
        return False # no special case for perfect numbers. They're not abundant

def is_sum(L, n):
    for i in L:
        for j in L:
            if i + j == n:
                return True
            elif i + j > n:
                break
    return False

def main():
    abundants = []
    answer = 0
    for i in range(24, 200):
        if is_abundant(i):
            abundants.append(i)
        if is_sum(abundants, i):
            answer += i
        if i % 1000 == 0:
            print i

    print answer



main()
