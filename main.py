import math
from exeption import MatrixException, EngineException, VectorException, PointExeption


class Matrix:
    def __init__(self, elements: list[list[int | float]]):
        self.matrix = elements
        self.width = len(elements)
        self.height = len(elements[0])
        for i in range(self.width-1):
            if len(self.matrix[i]) != len(self.matrix[i+1]):
                raise MatrixException.MATRIX_INCORRECT

    def transpose(self):
        return Matrix([[self.matrix[j][i] for j in range(self.width)] for i in range(self.height)])

    def zero_matrix(self, width: int, height: int):
        return Matrix([[0 for i in range(width)]for j in range(height)])

    def get_matrix_minor(self, index):
        return Matrix([self.matrix[i][:index] + self.matrix[i][index + 1:] for i in range(1, self.width)])

    def determinant(self):
        det = 0
        if self.height != self.width:
            raise MatrixException.MATRIX_NOT_SQUATER
        if self.height == 1:
            return self.matrix[0][0]
        else:
            for index in range(self.width):
                minor = Matrix.get_matrix_minor(self, index)
                det += self.matrix[0][index] * (-1) ** index * Matrix.determinant(minor)
            return det

    def inverse(self):
        if self.height != self.width:
            raise MatrixException.MATRIX_NOT_SQUATER
        det = self.determinant()
        if self.height == 2:
            return [[self.matrix[1][1] / det, -1 * self.matrix[0][1] / det],
                    [-1 * self.matrix[1][0] / det, self.matrix[0][0] / det]]
        inverse = []
        for r in range(self.width):
            new = []
            for c in range(self.height):
                minor = Matrix([row[:c] + row[c+1:] for row in (self.matrix[:r]+self.matrix[r+1:])])
                new.append((((-1) ** (r + c)) * Matrix.determinant(minor))/det)
            inverse.append(new)
        inverse_tr = Matrix(inverse).transpose().matrix
        return Matrix(inverse_tr)

    def identity(self, n):
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    def rotate_matrix(self, n, axis1, axis2, theta):
        """Rotate an n-dimensional matrix about two axes by angle theta."""
        cos = math.cos(theta)
        sin = math.sin(theta)
        # Create an n x n identity matrix.
        identity = Matrix.identity(self, n)
        # Fill the identity matrix with values that depend on the axes of rotation.
        identity[axis1][axis1] = cos
        identity[axis2][axis2] = cos
        identity[axis1][axis2] = -sin
        identity[axis2][axis1] = sin
        # Apply the rotation to the matrix and return the result.
        return identity

    def __add__(self, other):
        if type(other) != type(self) and other.isdigit() == 1:
            return Matrix([[self.matrix[i][j] + other
                            for j in range(self.width)]
                           for i in range(self.height)])
        if type(other) != type(self):
            raise EngineException.TYPE
        if self.height != other.height:
            raise MatrixException.MATRIX_WRONG_SIZES
        return Matrix([[self.matrix[i][j] + other.m[i][j]
                        for j in range(self.height)]
                       for i in range(self.width)])

    def __sub__(self, other):
        if type(other) != type(self) and other.isdigit() == 1:
            return Matrix([[self.matrix[i][j] - other
                            for j in range(self.width)]
                           for i in range(self.height)])
        if type(other) != type(self) and other.isdigit() != 1:
            raise EngineException.TYPE
        if self.height != other.height:
            raise MatrixException.MATRIX_WRONG_SIZES
        return Matrix([[self.matrix[i][j] - other.matrix[i][j]
                        for j in range(self.width)]
                       for i in range(self.height)])

    def gram(self):
        result = Matrix.zero_matrix(self, self.height, self.height)
        identity = Matrix.identity(self, self.width)
        for i in range(self.height):
            for j in range(self.width):
                result[i][j] = BilinearForm(identity, Vector(self.matrix[i]), Vector(self.matrix[j]))
        return result

    def __mul__(self, other):
        if type(other) != type(self) and other.isdigit() == 1:
            return Matrix([[self.matrix[i][j] * other
                            for j in range(self.width)]
                           for i in range(self.height)])
        if self.height != other.width:
            raise MatrixException.MATRIX_WRONG_SIZES
        result = [[0 for j in range(other.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(other.width):
                for k in range(self.height):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

    def __rmul__(self, o):
        return self.__mul__(o)

    def __repr__(self):
        return str(self.matrix).replace("],", "],\n")


class Vector(Matrix):
    def __init__(self, vector: [[[float]], Matrix]):
        self.vector = vector
        self.length = len(vector)

    def scalar(self, other):# scalar
        if self.length != other.lenght:
            raise VectorException.VECTOR_SIZE
        scal = 0
        for i in range(len(self.vector)):
            scal += self.vector[i]*other.vector[i]
        return scal

    def vector_product(self, other):
        if self.length != 3 or other.lenght != 3:
            raise VectorException.VECTOR_VECTORNOE
        m = Matrix([[1, 1, 1], self.vector, other.vector])
        r = [m.get_matrix_minor(0).determinant(), m.get_matrix_minor(1).determinant(),
             m.get_matrix_minor(2).determinant()]
        return r

    def dim(self):
        length = 0
        for i in range(len(self.vector)):
            length += self.vector[i]**2
        return length**0.5

    def size(self):
        return len(self.vector)

    def transpose(self):
        return Vector([[self.vector[j][i] for j in range(self.width)] for i in range(self.height)])

    def normalize(self):
        norma = Vector.dim(self.vector)
        if norma != 1:
            for i in self.vector:
                self.vector[i] = self.vector[i] / norma
        return self.vector

    def __mod__(self, other):
        return Vector.scalar(self, other)

    def __pow__(self, other):
        return Vector.vector_product(self, other)

    def __str__(self):
        return f'{self.vector}'


def BilinearForm(matrix: Matrix, Vector1: Vector, Vector2: Vector):
    if matrix.height == matrix.width and matrix.height == Vector1.length and matrix.width == Vector2.length:
        return sum([matrix[i][j] * Vector1[i] * Vector2[j]
                    for i in range(matrix.height)
                    for j in range(matrix.width)])
    raise MatrixException.TYPE


class Point:
    def __init__(self, point):
        self.point = point
        self.len = len(point)

    def __add__(self, other):
        if type(self) != type(other):
            return Point([self.point[i] + other.vector[i] for i in range(len(self.point))])
        raise PointExeption.POINT_TWO

    def __sub__(self, other):
        if type(self) != type(other):
            return Point([self.point[i] - other.vector[i] for i in range(len(self.point))])
        raise PointExeption.POINT_TWO

    def __str__(self):
        return f'{self.point}'


class VectorSpace:
    def __init__(self, basis: list[Vector]):
        self.basis = basis

    def __repr__(self):
        return str(self.basis).replace("],", "],\n")

    def scalar_product(self, vector1: Vector, vector2: Vector):
        return Matrix(vector1.transpose() * Matrix.gram(self.basis) * vector2.transpose())

    def as_vector(self: Vector, basis):
        if len(self.vector) != len(basis):
            raise VectorException.VECOR_BASIS
        coefficients = []
        for b in basis:
            c = (self * b) / b.normalite() ** 2
            coefficients.append(c)
        return Vector(coefficients)


class Cordinate_system:
    def __init__(self, point: Point, vectorspace: VectorSpace):
        self.Point = point
        self.Vectorspace = vectorspace




