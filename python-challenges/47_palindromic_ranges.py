import sys

def first_half(num_str):
    half = []
    for x in xrange(0, len(num_str) / 2):
        half.append(num_str[x])
    return half

def is_palindrome(num):
    num_str = str(num) 
    num_str_rev = num_str[::-1]

    if first_half(num_str) == first_half(num_str_rev):
        return True
    return False

def find_subranges(num1, num2):
    interesting = []
    for x in range(num1, num2 + 1):
        for y in range(x, num2 + 1):
            pal = []
            for subrange in range(x, y + 1):
                if is_palindrome(subrange):
                    pal.append(subrange)
            if len(pal) == 0 or len(pal) % 2 == 0:
                interesting.append(pal)

    print len(interesting)

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            find_subranges(*map(int, line.strip().split(' ')))
    sys.exit(0)
