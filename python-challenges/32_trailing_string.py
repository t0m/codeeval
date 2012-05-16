import sys

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        string, check = line.strip().split(',')
        if string[-len(check):] == check:
            print 1
        else:
            print 0
    sys.exit(0)
