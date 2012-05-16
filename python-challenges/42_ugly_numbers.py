import sys

cache = {}

def num_ugly(num_list):
    count = 0
    for num in num_list:
        if num == 0:
            count+=1
            continue
        elif num % 2 == 0:
            count+=1
            continue
        elif num % 3 == 0:
            count+=1
            continue
        elif num % 5 == 0:
            count+=1
            continue
        elif num % 7 == 0:
            count+=1
            continue
    return count


def permute(rem, level):
    ops = []
    if len(rem) == 1:
        ops.append(int(rem))
        return ops

    if rem in cache:
        for op in cache[rem]:
            ops.append(op)
        return ops

    ops.append(int(rem))

    for pos in range(1, len(rem)):
        next = rem[pos:]
        perm = permute(next, level + 1)
        for op in perm:
            add = int(rem[0:pos]) + int(op)
            sub = int(rem[0:pos]) - int(op)
            
            ops.append(add)
            ops.append(sub)
        cache[rem] = ops
    return ops

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            print num_ugly(permute(line.strip(), 0))

    sys.exit(0)
