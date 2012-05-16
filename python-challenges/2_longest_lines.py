import sys

if __name__ == '__main__':
    top_n = 0
    length_dict = dict()

    for line in open(sys.argv[1]):
        line = line.strip()
        if top_n == 0:
            top_n = int(line)
        else:
            length_dict[len(line)] = line

    keys = sorted(length_dict.keys(), reverse=True)
    for i in range(0, top_n):
        print length_dict[keys[i]]

    sys.exit(0)
