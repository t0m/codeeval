import sys

def prefix_eval(prefix_list):
	#start from the right
	prefix_list = prefix_list[::-1]
	stack = []
	for val in prefix_list:
		if val in ('+', '-', '/', '*'):
			num1 = stack.pop()
			num2 = stack.pop()
			if val == '+':
				stack.append(num1 + num2)
			elif val == '-':
				stack.append(num1 - num2)
			elif val == '/':
				stack.append(num1 / num2)
			elif val == '*':
				stack.append(num1 * num2)
		else:
			stack.append(int(val))
			
	return stack[0]

if __name__ == '__main__':
	for line in open(sys.argv[1]):
		if len(line.strip()) > 0:
			print prefix_eval(line.strip().split(' '))
	sys.exit(0)
