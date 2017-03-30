# euler14.py
"""

The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 40 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been definitively proved yet (Collatz problem) it is thought that all
starting numbers finish at 1.

Which number, under one million, produces the longest chain.

SOLVED
"""

def collatz(n):
	# takes a number and returns the length of the collatz sequence that it starts
	p = 1
	while n != 1:
		if n % 2 == 0:
			n = n/2
			p += 1
		else:
			n = 3 * n + 1
			p += 1

	return p

record = 10
answer = 13

for i in range(2, 1000000):
	p = collatz(i)
	if p > record:
		answer = i
		record = p
		print answer, '--', record

print answer
