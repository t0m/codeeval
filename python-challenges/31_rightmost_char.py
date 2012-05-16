import sys

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        string, char = line.strip().split(',')
        try:
            print string.index(char)
        except ValueError:
            print '-1'
    sys.exit(0)
