# class AVL:
#     class AVLNode:
#         def __init__(self, key, height, parent=None, left=None, right=None):
#             self.parent = parent
#             self.left = left
#             self.right = right
#             self.height = height
#             self.key = key
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self,x):
#
#     def search(self,x):
#         if self.root is None:
#             return False
#         elif

class BST:
    class BSTNode:
        def __init__(self, key, parent=None, left=None, right=None):
            self.parent = parent
            self.left = left
            self.right = right
            self.key = key

    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def search(self, x):
        if self.is_empty():
            return False, None
        else:
            node = self.root
            while node is not None:
                if x == node.key:
                    return True, node
                elif x > node.key:
                    node = node.right
                else:
                    node = node.left

            return False, None

    def insert(self, x):
        if self.is_empty():
            self.root = self.BSTNode(x)
        else:
            node = self.root
            while True:
                if x == node.key:
                    raise Exception("Key already present!")
                elif x > node.key:
                    if node.right is not None:
                        node = node.right
                    else:
                        node.right = self.BSTNode(x, parent=node)
                        break
                else:
                    if node.left is not None:
                        node = node.left
                    else:
                        node.left = self.BSTNode(x, parent=node)
                        break
        self.size += 1

    def inorder(self, node):
        if node is None:
            return []
        else:
            return self.inorder(node.left) + [node.key] + self.inorder(node.right)


class AVL:
    class AVLNode:
        def __init__(self, key, height, parent=None, left=None, right=None):
            self.parent = parent
            self.left = left
            self.right = right
            self.height = height
            self.key = key

    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def search(self, x):
        if self.is_empty():
            return False, None
        else:
            node = self.root
            while node is not None:
                if x == node.key:
                    return True, node
                elif x > node.key:
                    node = node.right
                else:
                    node = node.left

            return False, None

    def insert(self, x):
        if self.is_empty():
            self.root = self.AVLNode(x,1)
        else:
            node = self.root
            while True:
                if x == node.key:
                    raise Exception("Key already present!")
                elif x > node.key:
                    if node.right is not None:
                        node = node.right
                    else:
                        # node.right = self.AVLNode(x, parent=node)
                        break
                else:
                    if node.left is not None:
                        node = node.left
                    else:
                        # node.left = self.AVLNode(x, parent=node)
                        break
        self.size += 1

    def inorder(self, node):
        if node is None:
            return []
        else:
            return self.inorder(node.left) + [node.key] + self.inorder(node.right)


B = BST()
B.insert(5)
print(B.inorder(B.root))
B.insert(2)
print(B.inorder(B.root))
B.insert(3)
B.insert(4)
B.insert(1)
B.insert(6)
B.insert(8)
print(B.inorder(B.root), B.search(8))

