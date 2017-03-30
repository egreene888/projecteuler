"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time
import math

def d(n):
    """ Calculates the sum of the proper divisors of a number
    Doesn't use a particularly clever method """
    divsum = 1 # 1 is a factor for every number

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            # print '\t %d is a factor of %d' %(i, n)
            divsum += i

    return divsum

def main():
    t1 = time.time()
    answer = 0
    # print d(284)
    for i in range(2, 10000):
        # Check to see if the number is amicable.
        sumoffactors = d(i)
        doublesumoffactors = d(sumoffactors)
        # print '%d -> %d -> %d' %(i, sumoffactors, d(sumoffactors))

        if (i == doublesumoffactors) and (i != sumoffactors):
            print '%d and %d are amicable numbers' %(i, sumoffactors)
            answer += i

    print 'The answer is %d' %(answer)

    print 'And it took %f s to find it' %(time.time() - t1)

main()
