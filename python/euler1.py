# euler1.py
"""completed"""
# Solves problem 1 on project euler

# The problem
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000

sumofmultiples = 0
for i in range (1000):
	if i % 3 == 0 or i % 5 == 0:
		sumofmultiples += i

print sumofmultiples

# Solved