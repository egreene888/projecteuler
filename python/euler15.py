# euler15.py
"""
Starting in the top left corner of a 2 x 2 grid, and being only able to move left and right,
there are exactly 6 routes to the bottom right corner.

rrdd,
rdrd, rddr,
drrd, drdr,
ddrr

How many such routes are there on a 20 x 20 grid

SOLVED
"""

"""
These are the number of coin flip sequences that produce n heads and n tails

1 Coin

H
T

2 coins
HH
HT TH
TT

3 coins
HHH
HHT HTH THH
HTT THT TTH
TTT

4 coins

HHHH
HHHT HHTH HTHH THHH
HHTT HTHT HTTH THHT THTH TTHH
HTTT THTT TTHT TTTH
TTTT

5 coins
HHHHH
HHHHT HHHTH HHTHH HTHHH THHHH
HHHTT HHTHT HHTTH HTHHT HTHTH HTTHH THHHT THHTH THTHH TTHHH
HHTTT HTHTT HTTHT HTTTH THHTT THTHT THTTH TTHHT TTHTH TTTHH
HTTTT THTTT TTHTT TTTHT TTTTH
TTTTT

It's clearly just Pascal's triangle. So the answer to our problem is C(n, k)

= n! / k! (n - k)!

where n is double the size of the grid and k is the size of the grid
"""
def f(start, stop = 1):  # factorial function
	n = 1
	for i in range(start, stop, -1):
		n *= i
		# print i
	return n

def main():
	k = 20

	n = 2 * k
	# print f(5)
	# more brute-force way of computing the answer
	# answer = f(n) / (f(k) * f(n-k))

	answer2 = f(n, k) / f(n-k)
	# print f(n, k)

	# print answer
	print answer2
main()
