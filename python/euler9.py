# euler9.py

# Problem statement

"""
A Pythagorean triple is a set of natural numbers, a < b < c, such that
a^2 + b^2 = c^2

for example, 3^2 + 4^2 = 5^2, 9 + 16 = 25.

There exists exactly one pythagorean triple for which a + b + c = 1000.
Find the product abc.

SOLVED
"""
answer = 0
for m in range(1000):
	for n in range(1000):
		a = m**2 - n ** 2
		b = 2 * m * n
		c = m**2 + n**2
		if a <= 0 or b <= 0 or c <= 0:
			pass
		else:
			e = a
			f = b
			g = c
			while e + f + g <= 1000:
				if e + f + g == 1000:
					triple = [e, f, g]
					answer = e * f * g
					break
				else:
					e += a
					f += b
					g += c

		if answer:
			break
	if answer:
		break

print triple
print answer
