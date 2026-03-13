class NotSquareMatrixError(Exception):
    pass


class Matrix:

    def __init__(self, data):

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def add(self, m):

        if self.rows != m.rows or self.cols != m.cols:
            raise ValueError("Matrices must have same dimensions")

        return Matrix([
            [
                self.data[i][j] + m.data[i][j]
                for j in range(self.cols)
            ]
            for i in range(self.rows)
        ])

    def multiply(self, m):

        if self.cols != m.rows:
            raise ValueError("Invalid matrix multiplication")

        result = []

        for i in range(self.rows):

            row = []

            for j in range(m.cols):

                value = sum(
                    self.data[i][k] * m.data[k][j]
                    for k in range(self.cols)
                )

                row.append(value)

            result.append(row)

        return Matrix(result)

    def transpose(self):

        return Matrix([
            [
                self.data[j][i]
                for j in range(self.rows)
            ]
            for i in range(self.cols)
        ])