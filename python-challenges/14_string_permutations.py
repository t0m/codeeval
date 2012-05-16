import sys

def swap_chars(string, pos1, pos2):
	temp_val = string[pos1]
	string = string[:pos1] + string[pos2] + string[pos1+1:]
	string = string[:pos2] + temp_val + string[pos2+1:]
	return string


def permute(string):
	permutations = []

	#start in increasing order
	string = ''.join(sorted(string))
	permutations.append(string)
	while 1:
		#find largest index that has a bigger value to it's right
		largest_k = None
		for idx_k in range(0, len(string)-1):
			if string[idx_k + 1] > string[idx_k]:
				largest_k = idx_k
		
		#if there's none, we're done here
		if largest_k == None:
			return permutations
		
		#find the largest index starting from position k that has a bigger value than pos k
		largest_l = None
		for idx_l in range(largest_k, len(string)):
			if string[idx_l] > string[largest_k]:
				largest_l = idx_l

		#swap string[k] and string[l]
		string = swap_chars(string, largest_k, largest_l)

		#reverse from k + 1 to the end
		string = string[:largest_k + 1] + string[largest_k + 1:][::-1]

		permutations.append(string)

	return sorted(permutations)


if __name__ == '__main__':
	for line in open(sys.argv[1]):
		if len(line.strip()) > 0:
			print ','.join(permute(line.strip()))
	sys.exit(0)
