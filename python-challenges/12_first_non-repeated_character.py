import sys

def first_non_rep(word):
    char_counts = dict()
    for char in word:
        if char_counts.has_key(char):
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    for char in word:
        if char_counts[char] == 1:
            print char
            break

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        first_non_rep(line.strip())
    sys.exit(0)
