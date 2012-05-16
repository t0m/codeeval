import sys

def print_index(list, index):
    if index > len(list):
        return
    else:
        print list[len(list) - index]

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        chars = line.strip().split(' ')
        index = int(chars.pop())
        print_index(chars, index)


    sys.exit(0)
