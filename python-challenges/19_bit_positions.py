import sys

def check_bit_positions(n, p1, p2):
    binary = bin(n)[2::][::-1]
    if binary[p1 - 1] == binary[p2 - 1]:
        print "true"
    else:
        print "false"

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        n, p1, p2 = line.strip().split(',')
        check_bit_positions(int(n), int(p1), int(p2))
    sys.exit(0)
