class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)[1:-1]

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self) == 0

    def top(self):
        if self.is_empty():
            raise Exception("Stack Empty")
        else:
            return self.items[-1]

    def push(self, value):
        self.items += [value]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Empty")
        return self.items.pop()


class LinkedStack:
    # ---------------------Node for LL---------------------------------------------------------
    class _Node:
        __slots__ = ["_data", "_next"]  # This removes the dictionary associated with the object

        # Result of using __slots__:
        # Fast access to attributes
        # Saves memory space

        def __init__(self, data, next):
            self._data = data
            self._next = next

    # ------------------LinkedStack----------------------------------------------------------------
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, item):
        self._head = self._Node(item, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        else:
            answer = self._head._data
            self._head = self._head._next
            self._size -= 1
            return answer

    def top(self):
        if self._head is None:
            raise Exception("Stack Empty")
        return self._head._data

    def __str__(self):
        s = ""
        while self._head is not None:
            s += str(self._head._data)
            self._head = self._head._next
        return s

