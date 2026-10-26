# Task 5: Extending a Class
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        # Euclidean distance: sqrt of (dx^2 + dy^2)
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    # no __init__ here, Vector uses the one from Point

    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    p3 = Point(1, 2)
    print("p1:", p1)
    print("p2:", p2)
    print("p1 == p3:", p1 == p3)
    print("p1 == p2:", p1 == p2)
    print("distance p1 to p2:", p1.distance(p2))

    v1 = Vector(3, 4)
    v2 = Vector(-1, 2)
    v3 = v1 + v2
    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v3)
    print("v1 + v2 is a Vector:", isinstance(v3, Vector))
    print("v1 == Vector(3, 4):", v1 == Vector(3, 4))
    print("distance v1 to v2:", v1.distance(v2))
    # since Vector is a Point, distance works between the two kinds too
    print("distance v1 to origin:", v1.distance(Point(0, 0)))
