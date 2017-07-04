#euler16.py
"""
2^15 = 32768 and the sum of the digits is 3 + 2 + 7 + 6 + 8 = 26

What is the sum of the digits of the number 2^1000?

SOLVED
Solution basically uses type conversion. This would be harder in a language that
couldn't easily move between types.
"""

def main():
	giganticnumber = 2**1000
	giganticstring = str(giganticnumber)

	answer = 0
	for digit in giganticstring:
		answer += digit

	print answer

main()
