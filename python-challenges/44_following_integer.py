import sys

def map_num(num_str):
    num_map = dict()
    for char in num_str:
        num = int(char)
        if num > 0:
            if num_map.has_key(num):
                num_map[num] += 1
            else:
                num_map[num] = 1
    return num_map

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            num_map = map_num(line.strip())
            num = int(line.strip())
            for x in range(num + 1, 1000001):
                if map_num(str(x)) == num_map:
                    print x
                    break

    sys.exit(0)
