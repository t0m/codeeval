import sys

def print_reversed(line):
    if len(line) == 0:
        return
    split = line.split(' ')
    reversed_split = split[::-1]
    print ' '.join(reversed_split)

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        print_reversed(line.strip())
    sys.exit(0)
