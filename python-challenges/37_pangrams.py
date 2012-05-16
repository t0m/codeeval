import sys


if __name__ == '__main__':
    for line in open(sys.argv[1]):
        letters_left = set([char for char in 'abcdefghijklmnopqrstuvwxyz'])
        for char in line.lower():
            if char in letters_left:
                letters_left.remove(char)
        if len(letters_left) == 0:
            print('NULL')
        else:
            print(''.join(sorted(letters_left)))
    
    sys.exit(0)
