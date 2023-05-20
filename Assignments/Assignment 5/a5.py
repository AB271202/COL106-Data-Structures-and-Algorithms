class MaxHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self) == 0

    def parent(self, node):
        return (node - 1) // 2

    def left_child(self, node):
        return 2 * node + 1

    def right_child(self, node):
        return 2 * node + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapUp(self, node):
        while node != 0 and self.heap[self.parent(node)] < self.heap[node]:
            self.swap(node, self.parent(node))
            node = (node - 1) // 2

    def heapDown(self, node):
        """ Given a node u whose two children are heaps, we convert the whole subheap containing u to a heap """
        while node < len(self):
            left = self.left_child(node)
            right = self.right_child(node)
            if left < len(self) and right < len(self):
                x = self.heap[left]
                y = self.heap[right]
                if self.heap[node] > max(x, y):
                    break
                if x > y:
                    self.swap(node, self.left_child(node))
                    node = self.left_child(node)
                else:
                    self.swap(node, self.right_child(node))
                    node = self.right_child(node)
            elif left < len(self):
                if self.heap[left] > self.heap[node]:
                    self.swap(node, self.left_child(node))
                break
            else:
                break

    def extractMax(self):
        if self.is_empty():
            raise Exception("Empty heap!")
        answer = self.heap[0]
        self.swap(0, len(self) - 1)
        self.heap.pop()
        self.heapDown(0)
        return answer

    def enqueue(self, item):
        self.heap.append(item)
        self.heapUp(len(self) - 1)

    def __str__(self):
        return str(self.heap)[1:-1]


class Graph:
    def __init__(self, n):
        self.adjlist = [[] for i in range(n)]

    def add_edge(self, u, v, c):
        self.adjlist[u].append([c, v])
        self.adjlist[v].append([c, u])

    def getNeighbours(self, u):
        return self.adjlist[u]


def findMaxCapacity(n, links, s, t):
    G = Graph(n)
    capacity = [-1] * n
    capacity[s] = float('inf')
    for i in links:
        u, v, c = i
        G.add_edge(u, v, c)

    H = MaxHeap()
    for i in G.getNeighbours(s):
        H.enqueue((i[0], [s, i[1]]))  # O(d(s))
    while True:
        x = H.extractMax()
        if capacity[x[1][-1]] == -1:
            capacity[x[1][-1]] = x[0]
        else:
            continue
        if x[1][-1] == t:
            return x
        for j in G.getNeighbours(x[1][-1]):  # This step runs O(d(x)) times so |H|<2|E|
            if capacity[j[1]] == -1:
                H.enqueue((min(x[0], j[0]), x[1] + [j[1]]))


'''
Invariant: When Heap dequeues (c,path) {path[-1] for the first time} then c is the maximum capacity which can be transmitted between s and path[-1]
Proof by induction on the number of iterations
Base Case: For paths of length 1 between s and its neighbours, the maximum edge will correspond to the maximum path
Induction Step: let vertex v be enqueued. If there are greater capacity paths to that vertex, then portion of those must be present in the heap.
So by extracting the maximum one we have selected the best path.
'''

# print(findMaxCapacity(3, [(0, 1, 1), (1, 2, 1)], 0, 1))
# print(findMaxCapacity(4, [(0, 1, 30), (0, 3, 10), (1, 2, 40), (2, 3, 50), (0, 1, 60), (1, 3, 50)], 0, 3))
# print(findMaxCapacity(4, [(0, 1, 30), (1, 2, 40), (2, 3, 50), (0, 3, 10)], 0, 3))
# print(findMaxCapacity(5, [(0, 1, 3), (1, 2, 5), (2, 3, 2), (3, 4, 3), (4, 0, 8), (0, 3, 7), (1, 3, 4)], 0, 2))
# print(
#     findMaxCapacity(7, [(0, 1, 2), (0, 2, 5), (1, 3, 4), (2, 3, 4), (3, 4, 6), (3, 5, 4), (2, 6, 1), (6, 5, 2)], 0, 5))
