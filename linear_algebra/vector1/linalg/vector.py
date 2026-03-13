import math


class DimensionMismatchError(Exception):
    pass


class Vector:

    def __init__(self, data):
        self.data = data
        self.n = len(data)

    def add(self, v):
        if self.n != v.n:
            raise DimensionMismatchError("Vectors must have same dimension")

        return Vector([
            self.data[i] + v.data[i]
            for i in range(self.n)
        ])

    def sub(self, v):
        if self.n != v.n:
            raise DimensionMismatchError("Vectors must have same dimension")

        return Vector([
            self.data[i] - v.data[i]
            for i in range(self.n)
        ])

    def scalar_multiply(self, scalar):
        return Vector([
            x * scalar for x in self.data
        ])

    def dot(self, v):
        if self.n != v.n:
            raise DimensionMismatchError("Vectors must have same dimension")

        return sum(
            self.data[i] * v.data[i]
            for i in range(self.n)
        )

    def cross(self, v):

        if self.n != 3 or v.n != 3:
            raise ValueError("Cross product only defined for 3D vectors")

        x = self.data[1]*v.data[2] - self.data[2]*v.data[1]
        y = self.data[2]*v.data[0] - self.data[0]*v.data[2]
        z = self.data[0]*v.data[1] - self.data[1]*v.data[0]

        return Vector([x, y, z])

    def norm(self):
        return math.sqrt(
            sum(x*x for x in self.data)
        )