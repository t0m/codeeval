import sys

def parse(find):
    find_list = []
    current_ops = []
    escape = False
    for pos in range(0, len(find)):
        if find[pos] == '*':
            if escape == False:
                if len(current_ops) > 0:
                    find_list.append(''.join(current_ops))
                current_ops = []
            else:
                current_ops.pop()
                current_ops.append('*')
        elif find[pos] == '\\':
            current_ops.append('\\')
            escape = True
        else:
            current_ops.append(find[pos])
            escape = False

    if len(current_ops) > 0:
        find_list.append(''.join(current_ops))
    return find_list


def search(string, find_list):
    first = find_list[0]
    for x in range(0, len(string) - len(first) + 1):
        check_str = string[x:x+len(first)]
        if check_str == first:
            next = find_list[1:]
            if len(next) > 0:
                return search(string[x+len(first):], next)
            else:
                return "true"
    return "false"


if __name__ == '__main__':
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            string, find = line.strip().split(',')
            find_list = parse(find)
            print search(string, find_list)
    sys.exit(0)
