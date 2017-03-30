# euler17.py
"""
If the numbers from one to five are written out in words:
 'one', 'two', 'three', 'four', 'five', then there are
  3 + 3 + 5 + 4 + 4 = 19 letters used in total. 

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used? 

"""

# one two three four five six seven eight nine 
# takes an integer from 1 to 999 and returns the number of letters
def getletters(i): 
	l = 0
	string = str(i)
	#chop of all but the last three digits
	string = string[-3:]
	# deal with the umpteens
	if len(string) >= 2 and string[-2] == '1': 
		if string[-1] == '0': 
			l += 3 # == len('ten')
		elif string[-1] == '1' or string[-1] == '2': 
			l += 6 # == len('eleven') == len('twelve')
		elif string[-1] == '3' or string[-1] == '4' or string[-1] == '9' or string[-1] == '8':
			l += 8 # == len('thirteen') == len('fourteen') == len('nineteen') ==len('eighteen')
		elif string[-1] == '5' or string[-1] == '6': 
			l += 7 # == len('fifteen') == len('sixteen')
		elif string[-1] == '7' :
			l += 9 # == len('seventeen') 

	# deal with the ones and tens place
	else: 

		if string[-1] in ('1', '2', '6'):
			l += 3 # == len('one') == len('two') == len('six')
		elif string[-1] in ('4', '5', '9'): 
			l += 4 # == len('four') == len('five') == len('nine')
		elif string[-1] in ('3', '7', '8'): 
			l += 5 # == len('three') == len('seven') == len('eight')

		# tens place
		if len(string) > 1: 
			if string[-2] in ('2', '3' , '8', '9'): 
				l += 6 # == len('twenty') == len('thirty') == len('eighty') == len('ninety')
			elif string[-2] in ('4', '5', '6'):
				l += 5 # == len('forty') == len('fifty') == len('sixty')
			elif string[-2] in ('7',):
				l += 7 # == len('seventy')

	# deal with the hundreds place
	if len(string) > 2: 
		if string[-2:] != '00': 
			if string[-3] in('1', '2', '6'): 
				l += 13 # == len('one hundred and')
			elif string[-3] in ('3', '7', '8'):
				l += 15 # == len('three hundred and')
			elif string[-3] in ('4', '5', '9'):
				l += 14 # == len('four hundred and')
		else: 
			if string[-3] in ('1', '2', '6'):
				l += 10 # == len('one hundred')
			elif string[-3] in ('3', '7', '8'): 
				l += 12 # == len('three hundred')
			elif string[-3] in ('4', '5', '9'): 
				l += 11 # == len('four hundred')

	return l

a = 0
for i in range(1, 1000): 
	l = getletters(i)
	a += l
	print i , l , a
	

a += len('onethousand')
print a