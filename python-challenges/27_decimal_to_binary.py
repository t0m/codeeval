import sys

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        print bin(int(line.strip()))[2:]
    sys.exit(0)
