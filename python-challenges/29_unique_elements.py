import sys


def kill_dupes(dupe_list):
    dupe_check = set()
    dupe_free = []
    for number in dupe_list:
        if number not in dupe_check:
            dupe_check.add(number)
            dupe_free.append(number)
    print ",".join(dupe_free)

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        kill_dupes(line.strip().split(','))
    sys.exit(0)
