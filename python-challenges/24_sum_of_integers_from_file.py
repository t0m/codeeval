import sys

if __name__ == "__main__":
    sum_lines = 0
    for line in open(sys.argv[1]):
        sum_lines += int(line.strip())
    print sum_lines
    sys.exit(0)
