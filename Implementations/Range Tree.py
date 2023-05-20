class BST:
    class BSTNode:
        def __init__(self, key, parent=None, left=None, right=None):
            self.parent = parent
            self.left = left
            self.right = right
            self.key = key

        def is_leaf(self):
            return self.left is None and self.right is None

        def __str__(self):
            return str(self.key)

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

    def balancedBST(self, L):  # This takes O(n) time
        # L should be sorted
        if not L:
            return
        m = len(L) // 2
        self.insert(L[m])
        self.balancedBST(L[0:m])
        self.balancedBST(L[m + 1:])

    def getNode(self, val):
        found, node = self.search(val)
        if found:
            return node

    # # LOWEST COMMON ANCESTOR
    # def LCA(self, ptr, emp1, emp2):
    #     if ptr is None:
    #         return None
    #     if ptr == emp1 or ptr == emp2:
    #         return ptr
    #     sub1side = self.LCA(ptr.left, emp1, emp2)
    #     sub2side = self.LCA(ptr.right, emp1, emp2)
    #
    #     if sub1side and sub2side:
    #         return ptr
    #     elif sub1side:
    #         return sub1side
    #     else:
    #         return sub2side

    def lca(self, x, y):
        A = [x]
        B = [y]
        while x.parent is not None:
            A.append(x.parent)
            x = x.parent
        while y.parent is not None:
            B.append(y.parent)
            y = y.parent
        A.reverse()
        B.reverse()
        if A[-1] in B:
            return A[-1]
        if B[-1] in A:
            return B[-1]
        for i in range(min(len(A), len(B))):
            try:
                if A[i + 1] != B[i + 1]:
                    return A[i]
            except IndexError:
                return A[i]

    def first(self, node):
        while node.left is not None:
            node = node.left
        return node

    def last(self, node):
        while node.right is not None:
            node = node.right
        return node

    def getNodeP(self, x):
        node = self.root
        if x < self.first(self.root).key:
            return self.first(self.root)
        while True:
            if x == node.key:
                return node
            elif x > node.key:
                if node.right is not None:
                    node = node.right
                else:
                    return node
            else:
                if node.left is not None:
                    node = node.left
                else:
                    while node.parent.right != node:
                        node = node.parent
                    return node.parent

    def getNodeS(self, x):
        node = self.root
        if x > self.last(self.root).key:
            return self.last(self.root)
        while True:
            if x == node.key:
                return node
            elif x < node.key:
                if node.left is not None:
                    node = node.left
                else:
                    return node
            else:
                if node.right is not None:
                    node = node.right
                else:
                    while node.parent.left != node:
                        node = node.parent
                    return node.parent

    def getRange(self, node1, node2):
        if node1.key > node2.key:
            return []
        lca = self.lca(node1, node2)
        answer = []
        x = node1
        # while x != lca:
        #     if x == x.parent.left:
        #         answer.append(x.key)
        #         answer.extend(self.inorder(x.right))
        #     x = x.parent
        # x = node2
        # answer.append(lca.key)
        # while x != lca:
        #     if x == x.parent.right:
        #         answer.append(x.key)
        #         answer.extend(self.inorder(x.left))
        #     x = x.parent
        # return answer
        if lca != node1:
            answer.append(node1.key)
            if node1.right is not None:
                answer.extend(self.inorder(node1.right))

            while x.parent != lca:
                if x == x.parent.left:
                    answer.append(x.parent.key)
                    answer.extend(self.inorder(x.parent.right))
                x = x.parent
        # print(answer)
        x = node2
        answer.append(lca.key)
        if lca != node2:
            while x.parent != lca:
                if x == x.parent.right:
                    answer.append(x.parent.key)
                    answer.extend(self.inorder(x.parent.left))
                x = x.parent
            answer.append(node2.key)
            if node2.left is not None:
                answer.extend(self.inorder(node2.left))
        return answer


L = [32, 68, 10, 71, 99, 86, 82, 29, 96, 52, 56, 88, 75, 26, 34, 43, 70, 22, 60, 39]
L.sort()

T = BST()
T.balancedBST(L)
print(T.inorder(T.root))
# print(T.root.key)
# print(T.root.left.key)
# print(T.root.left.left.key)
# print(T.root.left.right.key)
# print(T.root.right.key)
# print(T.root.right.right.key)
# print(T.root.right.left.key)
# print(T.lca(T.getNodeS(4), T.getNodeP(6)))
print(T.getRange(T.getNodeS(82.9), T.getNodeP(85.1)))
print(T.getNodeP(85.1))
print(T.getNodeS(82.9))
# print(T.getRange(T.getNodeS(2), T.getNodeP(6)))
# print(T.getRange(T.getNodeS(8.5), T.getNodeP(11.5)))
# print(T.getRange(T.getNodeS(6), T.getNodeP(7)))
# print(T.getRange(T.getNodeS(6), T.getNodeP(9)))
# print(T.getRange(T.getNodeS(1), T.getNodeP(9)))
# print(T.getRange(T.getNodeS(6), T.getNodeP(10)))
#
# print(T.getNodeP(9))
# print(T.getNodeP(7))
# print(T.getNodeP(6.55))
# print(T.getNodeP(3.9))
# print(T.getNodeP(-10))
# print(T.getNodeP(900))
# print(T.getNodeP(5.45))
# print(T.getNodeP(3))
#
# print(T.getNodeS(9))
# print(T.getNodeS(7))
# print(T.getNodeS(6.55))
# print(T.getNodeS(3.9))
# print(T.getNodeS(-10))
# print(T.getNodeS(900))
# print(T.getNodeS(5.45))
# print(T.getNodeS(3))
