# euler4.py
"""completed"""
# not a pretty implementation
# solves problem 4 of project euler

def main():
	largestPalindrome = 0
	for i in range (1000):
		for j in range(1000):
			product = str(i*j)
			start = product[0:len(product)/2]
			end = product[(len(product) - len(product)/2):len(product)]
			if start == end[::-1]:
				# print x
				if int(product) > largestPalindrome:
					largestPalindrome = int(product)

	print largestPalindrome

main()
