import sys

def print_multiple(x, n):
    multiple = 1
    check = n
    while check < x:
        multiple += 1
        check = n * multiple
    print check

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        x, n = line.strip().split(',')
        print_multiple(int(x), int(n))
    sys.exit(0)
