import sys

def scrub_chars(words, chars_to_scrub):
    scrubbed = []
    chars_to_scrub = set(chars_to_scrub)
    for char in words:
        if char not in chars_to_scrub:
            scrubbed.append(char)
    print ''.join(scrubbed).strip()

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        words, chars_to_scrub = line.strip().split(', ')
        scrub_chars(words, chars_to_scrub)
    sys.exit(0)
