class Vector2D():
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #  Other magic method
    # "__add__" for +
    # "__mul__" for *
    # "__truediv__" for /
    # "__floordiv__" for //
    # "__mod__" for  %
    # "__pow__" for  **
    # "__and__" for &
    # "__xor__" for ^
    # "__or__" for |
    # ------------------------
    # "__lt__" for <
    # "__le__" for <=
    # "__eg__" for ==
    # "__ne__" for !=
    # "__gt__" for >
    # "__ge__" for >=
    # ------------------------
    # "__getitem__"
    # "__setitem__"
    # ...
    def __add__(self, other):
        return Vector2D(self.x + other.x,
                        self.y + other.y)


v1 = Vector2D(5, 7)
v2 = Vector2D(3, 9)
result = v1 + v2
print("[{0}, {1}]".format(result.x, result.y))
