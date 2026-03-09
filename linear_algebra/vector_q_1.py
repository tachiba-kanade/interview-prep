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

    Vector addition, subtraction - done

    Scalar multiplication  - done

    Dot product - done

    Cross product (3D) - done

    Vector norm - done

    Matrix addition - done

    Matrix multiplication - done

    Matrix transpose - done

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

#LU decomposition, QR decomposition, Eigenvalues, Power iteration, SVD

import math 
import numpy as np
import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vector Visualization")

class Pygame3dEngine:
    def __init__(self):
        pygame.init()
        self.running = True
        self.display = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.font = pygame.font.SysFont('Comic Sans', 12)
        self.screen = pygame.display.set_mode(self.display, pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def check_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def flip(self):
        pygame.display.flip()
        self.screen.fill("black")
        self.clock.tick(60)
class DimensionMismatchError(Exception):
    # raise ValueError("Vectors must be of the same dimension")
    # TODO: to be imported and used as from my_linear_algebra import Matrix, Vector
    pass


class NotSquareMatrixError(Exception):
    pass


class Vector:
    def __init__(self, data):
        self.data = data
        self.n = len(data)

    def add(self, v1):
        if self.n != v1.n:
            raise ValueError("Vectors must be of the same dimension")
        result = [self.data[i] + v1.data[i] for i in range(self.n)]
        return result

    def sub(self, v1):
        if self.n != v1.n:
            raise ValueError("Vectors must be of the same dimension")
        result = [self.data[i] - v1.data[i] for i in range(self.n)]
        return result

    def scalar_multiply(self, scalar):
        result = [self.data[i] * scalar for i in range(self.n)]
        return result

    def dot(self, v1):
        if self.n != v1.n:
            raise ValueError("Vectors must be of the same dimension")
        result = sum(self.data[i] * v1.data[i] for i in range(self.n))
        return result
    
    def cross (self, v1):
        if self.n != 3 or v1.n != 3:
            raise ValueError("Cross product is only defined for 3D vectors")
        x = self.data[1] * v1.data[2] - self.data[2] * v1.data[1]
        y = self.data[2] * v1.data[0] - self.data[0] * v1.data[2]
        z = self.data[0] * v1.data[1] - self.data[1] * v1.data[0]
        return Vector([x, y, z])
    
    def norm(self):
        result = math.sqrt(sum(self.data[i] ** 2 for i in range(self.n)))
        return result


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def add(self, m1):
        if self.rows != m1.rows or self.cols != m1.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = [[self.data[i][j] + m1.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result
    
    # for matrix multiplication, the number of columns of the first matrix must equal the number of rows of the second matrix meaning 2x3 and 3x2 can be multiplied but not 2x3 and 2x3 so the new matrix will be 2x2
    def multiplication(self, m1):
        if self.cols != m1.rows:
            raise ValueError("Number of columns of the first matrix must equal number of rows of the second matrix")
        result = [[sum(self.data[i][k] * m1.data[k][j] for k in range(self.cols)) for j in range(m1.cols)] for i in range(self.rows)]
        return result
    
    # we can use  zip by python to swap values or numpy a.T for transpose 
    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return result
    

#TODO: use pygame to visualize vector and matrix operations, like showing the result of a cross product as a new vector in 3D space, or showing the effect of a matrix transformation on a shape.

