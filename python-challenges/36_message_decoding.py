import sys
import re

#get the next (num_chars) characters, ignoring line breaks
def get_next(num_chars, string):
    next_chars = ''
    moved = 0
    for char in string:
        if char not in ('\r', '\n'):
            next_chars += char
            num_chars -= 1
        moved += 1
        if num_chars == 0:
            break
    return next_chars, moved


def key_generator():
    key = 0
    level = 1
    while True:
        if key != 2**level - 1:
            form = '{0:0' + str(level) + 'b}'
            yield form.format(key)
            key += 1
        else:
            level += 1
            key = 0


if __name__ == "__main__":
    encoded = open(sys.argv[1]).read()
    pos = 0
    while pos < len(encoded.strip()):

        #find the message header
        header = ''
        while encoded[pos] not in ('0', '1'):
            header_str, moved = get_next(1, encoded[pos])
            header += header_str
            pos += moved

        #generate dict with a key value for each header
        header_key = dict()
        keygen = key_generator()
        for char in header:
            header_key[keygen.next()] = char

        #decode the message
        decoded = ''
        while True:
            key_len, moved = get_next(3, encoded[pos:])
            key_len = int(key_len, 2)
            pos += moved

            #break out if we've found the end of this message
            if key_len == 0:
                break

            #get all keys with this length
            while True:
                code, moved = get_next(key_len, encoded[pos:])
                pos += moved

                #break out of this loop and find the next set of encoded chars
                if code == '1' * key_len:
                    break

                decoded += header_key[code]

        print decoded

    sys.exit(0)
