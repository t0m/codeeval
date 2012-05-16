import sys
import re

#okay now let's try django's email verification
if __name__ == '__main__':
    email_re = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE
    )
    for line in open(sys.argv[1]):
        if re.match(email_re, line.strip()) is None:
            print 'false'
        else:
            print 'true'
        
    sys.exit(0)
