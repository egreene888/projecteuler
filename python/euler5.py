# euler5.py
"""completed"""
# problem statement
# 2520 is the smallest number that can be divided evenly by each of the numbers
# 1 to 10 without any remainder.

# What is the smallest positive number that can be is evenly divisible by all
# the numbers 1 through 20?

def main():
	n = 10
	n = 20

	factors = range(1, n+1)
	lcm = n

	while 1:
		lcm += n
		for i in factors:
			if lcm % i != 0:
				break
		else:
			print 'lcm = ', lcm
			break




main()

# the answer is 232792560
