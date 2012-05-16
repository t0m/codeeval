import sys

def is_prime(num):
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True

def print_primes(num):
    primes = [2]
    for x in xrange(3, num, 2):
        if is_prime(x):
            primes.append(x)
    print ','.join(map(str, primes))

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        print_primes(int(line.strip()))
    sys.exit(0)
