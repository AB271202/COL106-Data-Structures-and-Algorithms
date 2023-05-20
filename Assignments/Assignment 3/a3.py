def inRange(ymin, ymax, y):
    return ymin <= y <= ymax


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

    class XTreeNode:
        def __init__(self, key, Ytree=None, left=None, right=None, parent=None):
            self.Ytree = Ytree
            self.key = key
            self.left = left
            self.right = right
            self.parent = parent

        def is_leaf(self):
            return self.right is None and self.left is None

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, x, type):
        if type == 'y':
            if self.is_empty():
                self.root = self.BSTNode(x)
            else:
                node = self.root
                while True:
                    if x == node.key:
                        raise Exception("Key already present!")
                    elif x[1] > node.key[1]:
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
        else:
            if self.is_empty():
                self.root = self.XTreeNode(x)
            else:
                node = self.root
                while True:
                    if x == node.key:
                        raise Exception("Key already present!")
                    elif x > node.key:
                        if node.right is not None:
                            node = node.right
                        else:
                            node.right = self.XTreeNode(x, parent=node)
                            break
                    else:
                        if node.left is not None:
                            node = node.left
                        else:
                            node.left = self.XTreeNode(x, parent=node)
                            break

    def inorder(self, node):
        if node is None:
            return []
        else:
            return self.inorder(node.left) + [node.key] + self.inorder(node.right)

    def balancedBST(self, L, type):  # This takes O(n) time
        # L should be sorted
        if not L:
            return
        m = len(L) // 2
        self.insert(L[m], type)
        self.balancedBST(L[0:m], type)
        self.balancedBST(L[m + 1:], type)

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

    def getNodeP(self, x, boo):
        node = self.root
        if x < self.first(self.root).key[boo]:
            return self.first(self.root)
        while True:
            if x == node.key[boo]:
                return node
            elif x > node.key[boo]:
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

    def getNodeS(self, x, boo):
        node = self.root
        if x > self.last(self.root).key[boo]:
            return self.last(self.root)
        while True:
            if x == node.key[boo]:
                return node
            elif x < node.key[boo]:
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
        if node1.key[1] > node2.key[1]:
            return []
        lca = self.lca(node1, node2)
        answer = []
        x = node1

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

    def getRange2D(self, node1, node2, ymin, ymax):
        if node1.key > node2.key:
            return []
        lca = self.lca(node1, node2)
        # print(lca.key)
        answer = []
        x = node1

        if lca != node1:
            if inRange(ymin, ymax, node1.key[1]):
                answer.append(node1.key)
            if node1.right is not None:
                T = node1.right.Ytree
                if ymin > T.last(T.root).key[1] or ymax < T.first(T.root).key[1]:
                    pass
                else:
                    answer.extend(T.getRange(T.getNodeS(ymin, 1), T.getNodeP(ymax, 1)))

            while x.parent != lca:
                # print(x.key)
                if x == x.parent.left:
                    if inRange(ymin, ymax, x.parent.key[1]):
                        answer.append(x.parent.key)
                    if x.parent.right is not None:
                        T = x.parent.right.Ytree
                        if ymin > T.last(T.root).key[1] or ymax < T.first(T.root).key[1]:
                            pass
                        else:
                            answer.extend(T.getRange(T.getNodeS(ymin, 1), T.getNodeP(ymax, 1)))
                x = x.parent
        # print(answer)
        x = node2
        if inRange(ymin, ymax, lca.key[1]):
            answer.append(lca.key)
        if lca != node2:
            while x.parent != lca:
                if x == x.parent.right:
                    if inRange(ymin, ymax, x.parent.key[1]):
                        answer.append(x.parent.key)
                    if x.parent.left is not None:
                        T = x.parent.left.Ytree
                        if ymin > T.last(T.root).key[1] or ymax < T.first(T.root).key[1]:
                            pass
                        else:
                            answer.extend(T.getRange(T.getNodeS(ymin, 1), T.getNodeP(ymax, 1)))
                x = x.parent
            if inRange(ymin, ymax, node2.key[1]):
                answer.append(node2.key)
            if node2.left is not None:
                T = node2.left.Ytree
                if ymin > T.last(T.root).key[1] or ymax < T.first(T.root).key[1]:
                    pass
                else:
                    answer.extend(T.getRange(T.getNodeS(ymin, 1), T.getNodeP(ymax, 1)))

        return answer


def join(A, B):
    i = j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i][1] > B[j][1]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    if i == len(A):
        C.extend(B[j:])
    elif j == len(B):
        C.extend(A[i:])
    return C


def merge(tree1, tree2, node):
    A = tree1.inorder(tree1.root)
    B = tree2.inorder(tree2.root)
    C = join(A, B)
    T = BST()
    T.balancedBST(C, 'y')
    T.insert(node.key, 'y')
    return T


class PointDatabase:

    def getYTree(self, node):
        if node is None:
            return BST()
        if node.is_leaf():
            node.Ytree = BST()
            node.Ytree.insert(node.key, 'y')
            return node.Ytree
        else:
            T = merge(self.getYTree(node.left), self.getYTree(node.right), node)
            # print(T.inorder(T.root))
            node.Ytree = T
            return T

    def __init__(self, pointlist):
        if not pointlist:
            self.T = BST()
            return
        pointlist.sort()
        self.T = BST()
        self.T.balancedBST(pointlist, "x")
        # print(self.T.inorder(self.T.root), self.T.root.key,self.T.root.left.key,self.T.root.right.key,self.T.root.left.left.key)
        self.getYTree(self.T.root)
        # print(self.T.root.Ytree.inorder(self.T.root.Ytree.root))

    def searchNearby(self, q, d):
        if self.T.is_empty():
            return []
        xmin = q[0] - d
        xmax = q[0] + d
        ymin = q[1] - d
        ymax = q[1] + d
        if xmin > self.T.last(self.T.root).key[0] or xmax < self.T.first(self.T.root).key[0]:
            return []

        return self.T.getRange2D(self.T.getNodeS(xmin, 0), self.T.getNodeP(xmax, 0), ymin, ymax)


#pointDbObject = PointDatabase([(1, 6), (2, 4), (3, 7), (4, 9), (5, 1), (6, 3), (7, 8), (8, 10),
#                                (9, 2), (10, 5)])
#print(pointDbObject.searchNearby((5, 5), 0))
# print(pointDbObject.searchNearby((4, 8), 2))
# print(pointDbObject.searchNearby((6, 2), 2))
# print(pointDbObject.searchNearby((10, 2), 1.5))
# a=PointDatabase([(1, 6), (2, 4), (3, 7), (4, 9), (5, 1), (6, 3), (7, 8), (8, 10), (9, 2), (10, 5)])
# print(a.searchNearby((84,48),1.1))
# b=PointDatabase([(32, 72), (68, 52), (10, 59), (71, 85), (99, 96), (86, 7), (82, 65), (29, 50), (96, 49), (52, 94), (56, 93), (88, 78), (75, 98), (26, 56), (34, 26), (43, 55), (70, 80), (22, 30), (60, 47), (39, 70)])
# print(b.searchNearby((84,48),1.1))
