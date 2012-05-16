import sys

def is_palindrome(num_str):
    palindrome = True
    rev_str = num_str[::-1]
    for x in range(0, len(num_str)/2):
        if num_str[x] != rev_str[x]:
            palindrome = False
            break
    return palindrome

def pal_iters(num):
    iterations = 0
    check_pal = 0
    while iterations < 1000:
        iterations += 1
        rev_num = num[::-1]    
        check_pal = int(num) + int(rev_num)
        if is_palindrome(str(check_pal)):
            break
        num = str(int(num) + int(rev_num))
        
    print ' '.join([str(iterations), str(check_pal)])

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        pal_iters(line.strip())
    
    sys.exit(0)
