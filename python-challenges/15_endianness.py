import sys

if __name__ == '__main__':
    if sys.byteorder == 'big':
        print 'BigEndian'
    else:
        print 'LittleEndian'
    sys.exit(0)
