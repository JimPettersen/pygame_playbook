from math import sqrt, cos, sin, radians


class Vector:
    UP = None
    DOWN = None
    LEFT = None
    RIGHT = None
    ZERO = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Vector(self.x // scalar, self.y // scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def distance_to(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    @property
    def length(self):
        return sqrt(self.x**2 + self.y**2)

    @property
    def length_squared(self):
        return self.x**2 + self.y**2

    def normalize(self):
        l = self.length
        if l == 0:
            return Vector(0, 0)
        return Vector(self.x / l, self.y / l)

    def rotate(self, angle_degrees):
        theta = radians(angle_degrees)
        return Vector(
            self.x * cos(theta) - self.y * sin(theta),
            self.x * sin(theta) + self.y * cos(theta),
        )

    def perpendicular(self):
        return Vector(-self.y, self.x)

    def clamp(self, min_val, max_val):
        return Vector(
            min(max_val, max(min_val, self.x)), min(max_val, max(min_val, self.y))
        )

    @staticmethod
    def lerp(a, b, t):
        return a + (b - a) * t


Vector.UP = Vector(0, -1)
Vector.DOWN = Vector(0, 1)
Vector.LEFT = Vector(-1, 0)
Vector.RIGHT = Vector(1, 0)
Vector.ZERO = Vector(0, 0)
