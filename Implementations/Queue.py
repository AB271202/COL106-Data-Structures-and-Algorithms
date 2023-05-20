class Queue:
    # ---------------------Node for Queue---------------------------------------------------------
    class _Node:
        __slots__ = ["data", "next"]  # This removes the dictionary associated with the object

        # Result of using __slots__:
        # Fast access to attributes
        # Saves memory space

        def __init__(self, data, next):
            self.data = data
            self.next = next

    # ------------------Queue----------------------------------------------------------------
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def front(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        return self.head.data

    def enqueue(self, value):
        if self.head is None and self.tail is None:
            self.head = self.tail = self._Node(value, None)
        else:
            self.tail.next = self._Node(value, None)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        x = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return x

    def __str__(self):

        s = "F "
        x = self.head
        #Note that here I could not just keep changing x -> then it destroys the list
        while x is not None:
            s += str(x.data) + " "
            x = x.next
        s += "R"
        return s

if __name__=="__main__":
    qu = Queue()
    qu.enqueue(5)
    qu.enqueue(6)
    print(qu)
    print(qu.front())
    qu.enqueue(28)
    qu.enqueue(22)
    print(qu)
    print(qu.dequeue())

    print(qu)
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.is_empty())
