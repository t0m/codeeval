import sys

def print_sums(numbers, target):
    numbers = map(int, numbers)
    target = int(target)
    lookup_set = set(numbers)
    # set of tuples so order doesn't matter and dupes are auto eliminated
    sums_set = set()

    for num in numbers:
        diff = target - num
        
        if diff in lookup_set and diff != num:
            first, second = [n for n in sorted([num, diff])]
            sums_set.add((first, second))
    
    sums_list = sorted(sums_set)
    print_list = list()
    for tup in sums_list:
        print_list.append(','.join([str(n) for n in tup]))

    if len(print_list) > 0:
        print ';'.join(print_list)
    else:
        print 'NULL'

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            numbers, target = line.strip().split(';')
            numbers = numbers.split(',')
            print_sums(numbers, target)
            
    sys.exit(0)
