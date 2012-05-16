import sys

class Node:
    def search(self, num):
        if num == self.num:
            return self
        if num < self.num:
            if self.left is None:
                return None
            else:
                return self.left.search(num)
        if num > self.num:
            if self.right is None:
                return None
            else:
                return self.right.search(num)

    def add(self, num):
        if num > self.num:
            if self.right == None:
                self.right = Node(num, self)
            else:
                self.right.add(num)
        else:
            if self.left == None:
                self.left = Node(num, self)
            else:
                self.left.add(num)

    def __init__(self, num, parent):
        self.num = num
        self.parent = parent
        self.left = None
        self.right = None
        if parent == None:
            self.level = 0
        else:
            self.level = parent.level + 1
            
class BinarySearchTree:

    def search(self, num):
        return self.root.search(num)

    def add(self, num):
        if self.root == None:
            self.root = Node(num, None)
        else:
            self.root.add(num)

    def __init__(self):
        self.root = None
        self.add(30)
        self.add(8)
        self.add(52)
        self.add(3)
        self.add(20)
        self.add(10)
        self.add(29)
    

def print_lca(node1, node2):
    # traverse up from either node1 or node2 until they are at the same level
    while node1.level > node2.level:
        node1 = node1.parent
    while node2.level > node1.level:
        node2 = node2.parent

    # traverse up together until they converge
    while node2.num != node1.num:
        node2 = node2.parent
        node1 = node1.parent

    print node2.num
    

        
if __name__ == '__main__':
    tree = BinarySearchTree()
    for line in open(sys.argv[1]):
        left, right = map(int, line.strip().split(' '))
        node1 = tree.search(left)
        node2 = tree.search(right)
        print_lca(node1, node2)
    sys.exit(0)
