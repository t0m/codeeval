import sys
import os

def fizzbuzz(numbers):
    for line in numbers:
        a = int(line[0])
        b = int(line[1])
        n = int(line[2]) + 1

        for x in xrange(1, n):
            to_print = []
            if x % a == 0:
                to_print.append('F')
            if x % b == 0:
                to_print.append('B')
            if len(to_print) == 0:
                to_print.append(str(x))
            to_print.append(' ')
            sys.stdout.write(''.join(to_print))
        sys.stdout.write(os.linesep)

if __name__ == "__main__":
    numbers = [line.strip().split(' ') for line in open(sys.argv[1])]
    fizzbuzz(numbers)
    sys.exit(0)
