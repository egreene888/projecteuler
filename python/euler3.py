# euler3.py

# Solves problem 3 on Project Euler

# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143

"""SOLVED"""

# the idea for finding the largest prime factor of n is to successively divide n
# by integers, and then check to see if the integers in question are prime.

def main():
	# n = 27
	# n = 13195
	n = 600851475143
	largestprimefactor = 2
	i = 3
	while True:
		if n % i == 0:
			for j in range(2, i/2):
				if i % j == 0:
					break
			else:
				largestprimefactor = i
				n = n/i
		if i > n:
			break
		i += 2

	print "%d is the largest prime factor" %(largestprimefactor)

main()
