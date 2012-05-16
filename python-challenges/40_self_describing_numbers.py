import sys

def check_self_describing(num_str):
    count_dict = dict()
    self_describing = 1

    for char in num_str:
        num = int(char)
        if count_dict.has_key(num):
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for pos, char in enumerate(num_str):
        num = int(char)
        if not count_dict.has_key(pos):
            if num != 0:
                self_describing = 0
                break
        else:
            if count_dict[pos] != num:
                self_describing = 0
                break

    print self_describing

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        check_self_describing(line.strip())
    sys.exit(0)
