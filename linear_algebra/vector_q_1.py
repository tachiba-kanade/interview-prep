"""
Custom Linear Algebra Library
Build your own mini linear algebra module from scratch.
Build your own set of functions or a simple class to represent and manipulate vectors and matrices

Add, sub, multiply, and divide vectors and matrices
Calculate the dot product and cross product of vectors
Calculate the determinant and inverse of matrices
Calculate the eigenvalues and eigenvectors of matrices

q1. How will you represent a Vector?

- As a list?

- As a class?

q2. How will you represent a Matrix?

- As a list of lists?

- As a class with attributes like rows and cols?

q3. Can you implement the following operations?

    Vector addition, subtraction

    Scalar multiplication

    Dot product

    Cross product (3D)

    Vector norm

    Matrix addition

    Matrix multiplication

    Matrix transpose

q4. Can your library:
    - Check dimension compatibility automatically?
    - Raise proper errors?

q5. Can you implement:

    - Determinant (2x2 and 3x3)
    - Matrix inverse
    - Gaussian elimination
    - Advanced:Overload operators like +, -, *, @?

Final Challenge

    Can someone import your file like this?  from my_linear_algebra import Matrix, Vector
    And use it naturally?

"""

# methods, dimensions, data
# Vector
# add, sub, mul, div, dot, cross, norm

# data, rows, cols, methods
# Matrices
# transpose, determinant, inverse, gaussian elimination


class DimensionMismatchError(Exception):
    pass


class NotSquareMatrixError(Exception):
    pass


class SingularMatrixError(Exception):
    pass

# Utilities 
def _is_numeric(value):
    return isinstance(value, (int, float))


def _validate_numeric_iterable(iterable):
    for value in iterable:
        if not _is_numeric(value):
            raise TypeError("All elements must be numeric.")


def _validate_rectangular(data):
    if not data:
        raise ValueError("Matrix cannot be empty.")

    row_length = len(data[0])
    for row in data:
        if len(row) != row_length:
            raise ValueError("Matrix rows must all have the same length.")


def _deep_copy_2d(data):
    return [row[:] for row in data]

class Vector:
    def __init__(self, data):
        if not hasattr(data, "__iter__"):
            raise TypeError("Vector must be initialized with an iterable.")

        data = list(data)
        if len(data) == 0:
            raise ValueError("Vector cannot be empty.")

        _validate_numeric_iterable(data)

        self._data = tuple(data)  # Immutable storage
        self._dim = len(data)

    @property
    def dimension(self):
        return self._dim

    def __repr__(self):
        return f"Vector({list(self._data)})"

    def __eq__(self, other):
        return isinstance(other, Vector) and self._data == other._data

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dimension != other.dimension:
            raise DimensionMismatchError("Vectors must have same dimension.")
        return Vector([a + b for a, b in zip(self._data, other._data)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dimension != other.dimension:
            raise DimensionMismatchError("Vectors must have same dimension.")
        return Vector([a - b for a, b in zip(self._data, other._data)])

    def __mul__(self, scalar):
        if not _is_numeric(scalar):
            return NotImplemented
        return Vector([a * scalar for a in self._data])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if not _is_numeric(scalar):
            return NotImplemented
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Vector([a / scalar for a in self._data])

    def __matmul__(self, other):
        return self.dot(other)

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Dot product requires another Vector.")
        if self.dimension != other.dimension:
            raise DimensionMismatchError("Vectors must have same dimension.")
        return sum(a * b for a, b in zip(self._data, other._data))

    def cross(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Cross product requires another Vector.")
        if self.dimension != 3 or other.dimension != 3:
            raise DimensionMismatchError("Cross product is defined only for 3D vectors.")

        a1, a2, a3 = self._data
        b1, b2, b3 = other._data

        return Vector([
            a2 * b3 - a3 * b2,
            a3 * b1 - a1 * b3,
            a1 * b2 - a2 * b1
        ])

    def norm(self):
        return sum(a * a for a in self._data) ** 0.5
class Matrix:
    def __init__(self, data):
        if not hasattr(data, "__iter__"):
            raise TypeError("Matrix must be initialized with an iterable of iterables.")

        data = [list(row) for row in data]

        _validate_rectangular(data)

        for row in data:
            _validate_numeric_iterable(row)

        self._data = _deep_copy_2d(data)
        self._rows = len(data)
        self._cols = len(data[0])

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def shape(self):
        return (self._rows, self._cols)

    def __repr__(self):
        return f"Matrix({self._data})"

    def __eq__(self, other):
        return isinstance(other, Matrix) and self._data == other._data


    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.shape != other.shape:
            raise DimensionMismatchError("Matrices must have same shape.")

        result = [
            [a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self._data, other._data)
        ]
        return Matrix(result)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.shape != other.shape:
            raise DimensionMismatchError("Matrices must have same shape.")

        result = [
            [a - b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self._data, other._data)
        ]
        return Matrix(result)

    def __mul__(self, scalar):
        if not _is_numeric(scalar):
            return NotImplemented
        result = [[a * scalar for a in row] for row in self._data]
        return Matrix(result)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.cols != other.rows:
            raise DimensionMismatchError(
                "Matrix multiplication requires A.cols == B.rows."
            )

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                value = sum(
                    self._data[i][k] * other._data[k][j]
                    for k in range(self.cols)
                )
                row.append(value)
            result.append(row)

        return Matrix(result)


    def transpose(self):
        return Matrix([[self._data[j][i] for j in range(self.rows)]
                       for i in range(self.cols)])

    def determinant(self):
        if self.rows != self.cols:
            raise NotSquareMatrixError("Determinant is defined only for square matrices.")

        if self.rows == 2:
            a, b = self._data[0]
            c, d = self._data[1]
            return a * d - b * c

        if self.rows == 3:
            a, b, c = self._data[0]
            d, e, f = self._data[1]
            g, h, i = self._data[2]
            return (
                a * (e * i - f * h)
                - b * (d * i - f * g)
                + c * (d * h - e * g)
            )

        raise NotImplementedError("Determinant implemented only for 2x2 and 3x3.")

    def inverse(self):
        if self.rows != self.cols:
            raise NotSquareMatrixError("Inverse is defined only for square matrices.")

        det = self.determinant()
        if det == 0:
            raise SingularMatrixError("Matrix is singular and cannot be inverted.")

        if self.rows == 2:
            a, b = self._data[0]
            c, d = self._data[1]
            return (1 / det) * Matrix([[d, -b], [-c, a]])

        raise NotImplementedError("Inverse implemented only for 2x2 matrices.")