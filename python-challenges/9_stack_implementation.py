import sys

# list-backed interface as per requirements...
class LifoStack:
    stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def __init__(self):
        self.stack = []

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        stack = LifoStack()
        for num in line.strip().split(' '):
            stack.push(num)

        to_print = []
        for x in range(0, len(stack)):
            if x % 2 == 0:
                to_print.append(stack.pop())
            else:
                stack.pop()

        print(' '.join(to_print))
