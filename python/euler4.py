# euler4.py
"""completed"""
# not a pretty implementation
# solves problem 4 of project euler

palindromes = []

for i in range (1000):
	for j in range(1000):
		x = str(i*j)
		start = x[0:len(x)/2]
		end = x[(len(x) - len(x)/2):len(x)]
		if start == end[::-1]:
			# print x
			palindromes.append(int(x))

print max(palindromes)
