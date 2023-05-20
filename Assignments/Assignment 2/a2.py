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
        while node != 0 and self.heap[self.parent(node)] > self.heap[node]:
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
                if self.heap[node] < min(x, y):
                    break
                if x < y:
                    self.swap(node, self.left_child(node))
                    node = self.left_child(node)
                else:
                    self.swap(node, self.right_child(node))
                    node = self.right_child(node)
            elif left < len(self):
                if self.heap[left] < self.heap[node]:
                    self.swap(node, self.left_child(node))
                break
            else:
                break

    def extractMin(self):
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


def buildHeap(L):
    h = Heap()
    h.heap = [(0, 0, 0)] * len(L)
    for i in range(len(L) - 1, -1, -1):
        h.heap[i] = L.pop()
        h.heapDown(i)
    return h


# ----------------Class Heap ends----------------------------------

# Some Helper functions
def collide(m1, m2, v1, v2):
    v1new = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2new = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1new, v2new


def check_for_collision(v1, v2):
    return (v1 - v2) > 0


def collision_time(v1, v2, x1, x2):
    return abs((x2 - x1) / (v2 - v1))


def collision_position(v1, v2, x1, x2):
    return x1 + v1 * (collision_time(v1, v2, x1, x2))





# -------------------------------------------------

def listCollisions(M, x, v, m, T):
    dummy = list()
    zero = (float('inf'), 0, float('inf'))
    times = [zero] * len(M)
    for i in range(len(M) - 1):
        if check_for_collision(v[i], v[i + 1]) and collision_time(v[i], v[i + 1], x[i], x[i + 1]) <= T:
            dummy.append((collision_time(v[i], v[i + 1], x[i], x[i + 1]), i,
                          collision_position(v[i], v[i + 1], x[i], x[i + 1])))
    h = buildHeap(dummy)
    # print("Initial heap: ", h)
    answer = []
    noc = 0
    while noc < m and not h.is_empty():
        cur = h.extractMin()
        i = cur[1]
        t = cur[0]

        # Check if the collision is invalid

        if times[i + 1] != zero and times[i] == zero:
            if times[i + 1][0] != cur[0]:
                continue
        elif times[i] != zero and times[i + 1] == zero:
            if times[i][2] != cur[0]:
                continue
        elif times[i] != zero and times[i + 1] != zero:
            if min(times[i + 1][0], times[i][2]) != cur[0]:
                continue

        # If time of collision exceeded T
        if T < cur[0]:
            break

        # For valid collisions
        answer.append(cur)  
        noc += 1
        x[i] = x[i + 1] = cur[2]
        v[i], v[i + 1] = collide(M[i], M[i + 1], v[i], v[i + 1])
        times[i] = (float('inf'), t, float('inf'))
        times[i + 1] = (float('inf'), t, float('inf'))

        if i - 1 >= 0:
            if check_for_collision(v[i - 1], v[i]):
                position1 = x[i - 1] + (t - times[i - 1][1]) * v[i - 1]
                h.enqueue((t + collision_time(v[i - 1], v[i], position1, x[i]), i - 1,
                           collision_position(v[i - 1], v[i], position1, x[i])))
                times[i] = (t + collision_time(v[i - 1], v[i], position1, x[i]), times[i][1], float('inf'))

        if i + 2 < len(M):
            if check_for_collision(v[i + 1], v[i + 2]):
                position2 = x[i + 2] + (t - times[i + 2][1]) * v[i + 2]
                h.enqueue((t + collision_time(v[i + 1], v[i + 2], x[i + 1], position2), i + 1,
                           collision_position(v[i + 1], v[i + 2], x[i + 1], position2)))
                times[i + 1] = (
                    float('inf'), times[i + 1][1], t + collision_time(v[i + 1], v[i + 2], x[i + 1], position2))
        # print("Heap status: ", h, "\ntimes", times, "\nvelocities", v, "\npositions", x, "\n\n")
    return answer


# print(listCollisions([1.0, 5.0], [1.0, 2.0], [3.0, 5.0], 100, 100.0))
# print(listCollisions([1.0, 1.0, 1.0, 1.0], [-2.0, -1.0, 1.0, 2.0], [0.0, -1.0, 1.0, 0.0], 5, 5.0))
# print(listCollisions([10000.0, 1.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.0, -1.0], 6, 10.0))
# print(listCollisions([10000.0, 1.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.0, -1.0], 100, 1.5))
# print(listCollisions([1, 1, 1, 1], [-2, -1, 1, 2], [10, 1, -1, -10], 10, 3))
