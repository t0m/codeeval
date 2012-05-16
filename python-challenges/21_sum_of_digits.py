import sys

def print_sum_digits(num):
    sum_d = 0
    for digit in str(num):
        sum_d += int(digit)
    print sum_d

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        print_sum_digits(line.strip())
    sys.exit(0)
