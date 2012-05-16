import sys

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        binary = bin(int(line.strip()))
        print len([x for x in binary if x == '1'])
    sys.exit(0)
