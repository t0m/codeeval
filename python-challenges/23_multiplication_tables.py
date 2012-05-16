import sys
import os

def print_table(rows, columns):
    for row in xrange(1, rows + 1):
        for column in xrange(1, columns + 1):
            sys.stdout.write(str(column * row).rjust(4))
        sys.stdout.write(os.linesep)

if __name__ == '__main__':
    print_table(12, 12)
    sys.exit(0)
