class Heap:
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

L = [(5, 2), (5, 3), (2, 3), (1, 4), (7, 3), (12, 2), (62, 2), (17, 1)]
H = Heap()
H=Heap()
for i in range( 10):
    H.enqueue(i)
print(H)
for i in range(10):
    print(H.extractMax())

