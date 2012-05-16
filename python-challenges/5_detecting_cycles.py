import sys

def find_cycle(num_list):
    """create two sliding windows of increasing length next to
    each other to check for duplicates
    """
    for check_length in range(1, len(num_list)/2 + 1):
        iterations = len(num_list) - check_length*2 + 1
        for position in range(0, iterations):
            behind = num_list[position:position+check_length]
            ahead = num_list[position+check_length:position+check_length*2]
            if behind == ahead:
                print ' '.join(behind)
                break
            
if __name__ == '__main__':
    for line in open(sys.argv[1]):
        num_list = line.strip().split(' ')
        if len(num_list) > 0:
            find_cycle(num_list)
    sys.exit(0)
