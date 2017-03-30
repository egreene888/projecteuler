# euler12.py

"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1, 3
6: 1, 2, 3
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 15, 28

As we can see, 28 is the first triangle number to have over 5 factors.

What is the first triangle number to have over 500 factors?

SOLVED
"""
# Set the number of factors necessary
n = 5
n = 50
# t and triangle are n and T such that we are on T_n
t = 1
triangle = 1

numfactors = 2

while numfactors < n:
	# find the next triangle number
	t += 1
	triangle += t

	# every number has 1 and itself as a factor, so we start the counter at 2
	numfactors = 2
	i = 2

	# factors come in pairs, so we only have to search the space up to n / f,
	# where f is the largest factor we've found
	limit = triangle / i
	while i < limit:
		# check if the number is a factor
		if triangle % i == 0:
			# add the factor and it's pair
			numfactors += 2
			# reduce the limit to the factor's pair
			limit = triangle / i

		i += 1


	print triangle, '--' , numfactors

print 'answer = ', triangle
