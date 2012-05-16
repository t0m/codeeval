"""Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
"""

import sys

powers = {
    1 : "",
	2 : "Thousand",
	3 : "Million",
	4 : "Billion",
}

single_digits = {
	'1' : 'One',
	'2' : 'Two',
	'3' : 'Three',
	'4' : 'Four',
	'5' : 'Five',
	'6' : 'Six',
	'7' : 'Seven',
	'8' : 'Eight',
	'9' : 'Nine',
}

special_double_digits = {
	'10' : 'Ten',
	'11' : 'Eleven',
	'12' : 'Twelve',
	'13' : 'Thirteen',
	'14' : 'Fourteen',
	'15' : 'Fifteen',
	'16' : 'Sixteen',
	'17' : 'Seventeen',
	'18' : 'Eighteen',
	'19' : 'Nineteen',
}

double_digits = {
	'2' : 'Twenty',
	'3' : 'Thirty',
	'4' : 'Forty',
	'5' : 'Fifty',
	'6' : 'Sixty',
	'7' : 'Seventy',
	'8' : 'Eighty',
	'9' : 'Ninety',
}

def get_sections(num_str):
	"""split the number up into number sections that can be evaluated as if 
	each is only 3 digits long"""
	sections = []
	section = ''
	counter = 0

	for pos in xrange(1, len(num_str) + 1):
		counter += 1
		section = num_str[-pos] + section
		if counter % 3 == 0 or pos == len(num_str):
			sections.insert(0, section)
			section = ''

	return sections

def get_text_value(piece):

	description = []
	if len(piece) == 3:
		if single_digits.has_key(piece[0]):
			description.append(single_digits[piece[0]])
			description.append("Hundred")
		description.append(get_text_value(piece[1:]))
	elif len(piece) == 2:
		if special_double_digits.has_key(piece):
			return special_double_digits[piece]
		elif double_digits.has_key(piece[0]):
			description.append(double_digits[piece[0]])
		description.append(get_text_value(piece[1:]))
	elif len(piece) == 1:
		if single_digits.has_key(piece):
			description.append(single_digits[piece])

	return ''.join(description)
		


def num_to_text(num_str):
	if num_str == '0':
		print 'ZeroDollars'
		return
	elif num_str == '1':
		print 'OneDollar'
		return
	
	number = []
	sections = get_sections(num_str)
	for unit, piece in enumerate(sections):
		number.append(get_text_value(piece))
		if piece != '000':
			number.append(powers.get(len(sections) - unit))
	print ''.join(number) + 'Dollars'


if __name__ == '__main__':
	test_cases = open(sys.argv[1], 'r')
	for line in test_cases:
		if len(line.strip()) > 0:
			num_to_text(line.strip())

	test_cases.close()
	sys.exit(0)
