import sys
import math

def check_jolly(num_list):
    jolly = True
    differences = set()
    prev = None
    
    for x in range(1, len(num_list)):
        if prev != None:
            difference = int(math.fabs(int(num_list[x]) - int(num_list[prev])))
            differences.add(difference)
        prev = x

    for x in range(1, len(num_list) - 1):
        if x not in differences:
            jolly = False

    if jolly:
        print 'Jolly'
    else:
        print 'Not jolly'


if __name__ == '__main__':
    for line in open(sys.argv[1]):
        check_jolly(line.strip().split(' '))
    sys.exit(0)
