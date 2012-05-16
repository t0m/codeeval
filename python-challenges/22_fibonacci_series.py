import sys

cache = {}

def fib(num):
    if num < 2:
        return num

    if cache.has_key(num):
        return cache[num]
    else:
        cache[num] = fib(num-1) + fib(num-2)
        return cache[num]

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        print fib(int(line))
    sys.exit(0)
