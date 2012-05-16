import sys

def check_happy(num_str):
    already_seen = set()
    already_seen.add(1)
    current_num = int(num_str)
    while current_num not in already_seen:
        already_seen.add(current_num)
        current_num = sum([int(i)*int(i) for i in str(current_num)])
    if current_num == 1:
        print '1'
    else:
        print '0'



if __name__ == "__main__":
    for line in open(sys.argv[1]):
        check_happy(line.strip())
    sys.exit(0)
