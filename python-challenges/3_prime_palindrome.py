import math
import sys

def first_half(num_str):
    half = []
    for x in xrange(0, len(num_str) / 2):
        half.append(num_str[x])
    return half

#good enough
def is_prime(n):
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def largest_palindrome(max):
    largest_prime_palindrome = 2
    for x in xrange(3, max, 2):
        chars = str(x)
        rev_chars = chars[::-1]
        if first_half(chars) == first_half(rev_chars):
            if is_prime(x):
                largest_prime_palindrome = x
    return largest_prime_palindrome

if __name__ == "__main__":
    print(largest_palindrome(1000))
    sys.exit(0)
