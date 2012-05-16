import sys

def find_dupe(num_list):
    dupe_check = set()
    dupe = None
    for num in num_list:
        if num in dupe_check:
            dupe = num
        else:
            dupe_check.add(num)

    print dupe

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            find_dupe(line.strip().split(';')[1].split(','))
    sys.exit(0)
