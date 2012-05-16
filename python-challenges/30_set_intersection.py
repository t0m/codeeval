import sys

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        left, right = [set(side.split(',')) for side in line.split(';')]
        intersection = sorted(left.intersection(right))
        print ",".join(intersection)
    sys.exit(0)
