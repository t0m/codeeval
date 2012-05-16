import sys

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if not n & 1: return False

    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

# without cheating and skipping 2
if __name__ == "__main__":
    check_num = 0
    sum_primes = 0
    count = 0
    while count < 1000:
        if (is_prime(check_num)):
            sum_primes += check_num
            count += 1
        check_num += 1
    print(sum_primes)
    sys.exit(0)
