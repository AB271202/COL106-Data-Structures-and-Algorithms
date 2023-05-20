class Point:
    def __init__(self, x, y):
        assert isinstance(x, (int, float)), "x is not valid"
        assert isinstance(y, (int, float)), "y is not valid"
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str(self.x) + " " + str(self.y)


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0: raise ValueError("step cannot be zero")
        if stop is None:
            start, stop = 0, start
        self.start = start
        self.step = step
        self.length = max(0, (stop - start + step - 1) // step)


X = Point(3, 4)
Y = Point(4, 5)
Z = X + Y
print(Z)
