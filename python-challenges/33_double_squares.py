import sys

def num_double_squares(num):
    possible_squares = list()
    lookup_set = set()
    
    current = 0
    square = 0
    while square <= num:
        possible_squares.append(square)
        lookup_set.add(square)
        current += 1
        square = current * current
    
    double_squares = set()
    for x in possible_squares:
        test_square = num - x
        if test_square in lookup_set:
            n1, n2 = [n for n in sorted([x, test_square])]
            double_squares.add((n1, n2))

    print len(double_squares)
            

if __name__ == '__main__':
    first = True
    for line in open(sys.argv[1]):
        if first:
            first = False
        else:
            num_double_squares(int(line.strip()))
    sys.exit(0)
