class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Tree:
    def __init__(self, key):
        self.root = Node(key)
        root.left = None
        root.right = None


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val, end=' '),

        # now recur on right child
        printInorder(root.right)


def printPreorder(root):
    if root:
        print(root.val, end=' ')
        printPreorder(root.left)
        printPreorder(root.right)


def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val, end=' ')


def find_height(root):
    if root == None:
        return 0
    lh = find_height(root.left)
    rh = find_height(root.right)
    lh += 1
    rh += 1
    if lh > rh:
        return lh
    else:
        return rh


def print_given_level(root):
    height = find_height(root)
    for i in range(1, height + 1):
        print_level_n(root, i)
        print()


def print_level_n(root, n):
    if root == None:
        return
    if n == 1:
        print(root.val, end=' ')
    if n > 1:
        print_level_n(root.left, n - 1)
        print_level_n(root.right, n - 1)


def print_level_order(root):
    if root == None:
        return
    q = []
    q.append(root)
    while len(q) > 0:
        node = q.pop(0)
        print(node.val)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_level_order(root)
