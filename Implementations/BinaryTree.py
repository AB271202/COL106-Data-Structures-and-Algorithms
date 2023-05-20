from Queue import Queue


class BinaryTreeNode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_root(self):
        return self.parent is None


class BinaryTree:
    def __init__(self):
        self.root = None

    def check_empty(self):
        return self.root is None

    def __len__(self):
        if self.root is not None:
            return 1 + len(self.root.left) + len(self.root.right)
        else:
            return 0

    # IMPORTANT!!
    def level_order_traversal(self):
        L = []
        if self.root is not None:
            Q = Queue()
            Q.enqueue(self.root)
            while not Q.is_empty():
                x = Q.dequeue()
                L.append(x)
                if x.left is not None: Q.enqueue(x.left)
                if x.right is not None: Q.enqueue(x.right)
        return L


class AlmostCompleteBinaryTree(BinaryTree):
    def add_node(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
