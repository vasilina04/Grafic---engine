import math
from lib.Exception.exeption import MatrixException, EngineException, VectorException, PointException, VectorSpaceException


PRECISION = 5


class Matrix:
    def __init__(self, elements: list[list[any]]):
        if len(elements) == 1 and len(elements[0]) == 0:
            raise EngineException(MatrixException.MATRIX_EMPTY)

        for i in range(len(elements)-1):
            if len(elements[i]) != len(elements[i+1]):
                raise EngineException(MatrixException.MATRIX_INCORRECT)

        self.matrix = elements
        self.width = len(elements[0])
        self.height = len(elements)

    def transpose(self):

        m = list()
        for i in range(0, self.width):
            width = list()
            for j in range(self.height):
                width.append(self.matrix[j][i])
            m.append(width)
        if isinstance(self, Vector):
            return Vector(m)
        return Matrix(m)

    def norm(self):
        result = 0
        for i in range(self.height):
            for j in range(self.width):
                result += self.matrix[i][j]**2
        return round(result**0.5, PRECISION)

    @classmethod
    def zero_matrix(cls, width: int, height: int):
        return cls([[0 for _ in range(width)]for _ in range(height)])

    def get_matrix_minor(self, index: int):
        return Matrix([self.matrix[i][:index] + self.matrix[i][index + 1:] for i in range(1, self.width)])

    def determinant(self):
        if not isinstance(self, Matrix):
            raise EngineException(EngineException.WRONG_USAGE)
        if self.height != self.width:
            raise EngineException(MatrixException.MATRIX_NOT_SQUARE)

        if isinstance(self.matrix[0][0], (int, float)):
            det = 0
            if self.height == 1:
                return self.matrix[0][0]
            else:
                for index in range(self.width):
                    minor = Matrix.get_matrix_minor(self, index)
                    det += self.matrix[0][index] * (-1) ** index * Matrix.determinant(minor)
                return round(det, PRECISION)
        else:
            result = Vector([0, 0, 0])
            for index in range(self.width):
                m = Matrix.get_matrix_minor(self, index)
                det = m.determinant()
                result = round(result + (-1) ** index * det * self.matrix[0][index], PRECISION)
            return result

    def inverse(self):
        if not isinstance(self, Matrix):
            raise EngineException(EngineException.WRONG_USAGE)
        if self.height != self.width:
            raise EngineException(MatrixException.MATRIX_NOT_SQUARE)

        det = self.determinant()
        if self.height == 2:
            return [[self.matrix[1][1] / det, -1 * self.matrix[0][1] / det],
                    [-1 * self.matrix[1][0] / det, self.matrix[0][0] / det]]
        inverse = []
        for r in range(self.width):
            new = []
            for c in range(self.height):
                minor = Matrix.get_matrix_minor(self, r)
                new.append(round((((-1) ** (r + c)) * Matrix.determinant(minor))/det, PRECISION))
            inverse.append(new)

        inverse_tr = Matrix(inverse).transpose().matrix

        return Matrix(inverse_tr)

    @classmethod
    def identity(cls, n):
        return cls([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    @classmethod
    def rotate_matrix(cls, n: int, axis1: int, axis2: int, theta: float):
        if not isinstance(n, int):
            raise EngineException(EngineException.WRONG_USAGE)
        if not (isinstance(axis1, int) and isinstance(axis2, int)):
            raise EngineException(EngineException.WRONG_USAGE)

        theta = theta * math.pi / 180
        cos = round(math.cos(theta), PRECISION)
        sin = round(math.sin(theta), PRECISION)
        identity = Matrix.identity(n)
        identity[axis1][axis1] = cos
        identity[axis2][axis2] = cos
        identity[axis1][axis2] = (-1) ** (axis1 + axis2) * sin
        identity[axis2][axis1] = (-1) ** (axis1 + axis2 + 1) * sin
        return identity

    def addition(self, other):
        if not isinstance(self, Matrix) or not isinstance(other, Matrix):
            raise EngineException(EngineException.WRONG_USAGE)

        if self.height != other.height:
            raise EngineException(MatrixException.MATRIX_WRONG_SIZES)

        return Matrix([[round(self.matrix[i][j] + other.matrix[i][j], PRECISION)
                        for j in range(self.width)]
                       for i in range(self.height)])

    def subtraction(self, other):
        if not isinstance(self, Matrix) or not isinstance(other, Matrix):
            raise EngineException(EngineException.WRONG_USAGE)

        if self.height != other.height:
            raise EngineException(MatrixException.MATRIX_WRONG_SIZES)

        return Matrix([[round(self.matrix[i][j] - other.matrix[i][j], PRECISION)
                        for j in range(self.width)]
                       for i in range(self.height)])

    def multiplication(self, other):
        if isinstance(self, Matrix) and isinstance(other, (float, int)):
            return Matrix([[round(self.matrix[i][j] * other, PRECISION)
                            for j in range(self.width)]
                           for i in range(self.height)])
        if isinstance(self, Matrix) and isinstance(other, Matrix) and self.height != other.width:
            raise EngineException(MatrixException.MATRIX_WRONG_SIZES)
        result = [[round(sum(x * y for x, y in zip(m1_r, m2_c)), PRECISION) for m2_c in zip(*other.matrix)] for m1_r in self.matrix]

        if isinstance(self, Vector) and isinstance(other, Vector):
            return Vector(result)

        return Matrix(result)

    def gram(self):
        if not isinstance(self, Matrix):
            raise EngineException(EngineException.WRONG_USAGE)
        if self.height != self.width:
            raise EngineException(MatrixException.MATRIX_NOT_SQUARE)

        result = Matrix.zero_matrix(self.height, self.height)
        identity = Matrix.identity(self.height)
        for i in range(self.height):
            for j in range(self.width):
                result[i][j] = round(BilinearForm(identity, Vector(self[i]), Vector(self[j])), PRECISION)
        return result

    def print(self):
        return str(self.matrix).replace("],", "],\n")

    def __add__(self, other):
        return Matrix.addition(self, other)

    def __sub__(self, other):
        return Matrix.subtraction(self, other)

    def __getitem__(self, index: int):
        return self.matrix[index]

    def __mul__(self, other):
        return Matrix.multiplication(self, other)

    def __rmul__(self, o):
        return self.__mul__(o)

    def __repr__(self):
        return Matrix.print(self)

    def __eq__(self, other):
        return self.matrix == other.matrix


class Vector(Matrix):
    def __init__(self, vector):
        if isinstance(vector, list):
            if isinstance(vector[0], list):
                super().__init__(vector)
                self.transpose_vector = True
                self.size = len(vector[0])
            else:
                v = list()
                v.append(vector)
                super().__init__(v)
                self.transpose_vector = False
                self.size = len(vector)
        elif isinstance(vector, int):
            vector = [[0 for _ in range(vector)]]
            super().__init__(vector)
            self.transpose_vector = False
        else:
            raise EngineException(EngineException.WRONG_USAGE)

    def scalar_product(self, other):
        if not isinstance(other, Vector):
            raise EngineException(EngineException.WRONG_USAGE)
        if not (other.width == self.width and other.height == self.height):
            raise EngineException(VectorException.VECTOR_SIZE)

        if self.transpose_vector != other.transpose_vector:
            other = other.transpose()
        if self.transpose_vector is True:
            result = 0
            for i in range(self.height):
                result += self.matrix[i][0] * other.matrix[i][0]
        else:
            result = 0
            for i in range(self.width):
                result += self.matrix[0][i] * other.matrix[0][i]
        return round(result, PRECISION)

    def normalize(self):
        norm = round(1/self.norm(), PRECISION)
        return self * norm

    def vector_product(self, other):
        if not isinstance(other, Vector):
            raise EngineException(VectorException.WRONG_USAGE)

        if self.transpose_vector != other.transpose_vector:
            other = other.transpose()

        if self.size != other.size and self.size != 3:
            raise EngineException(VectorException.VECTOR_SIZE)

        result = Matrix([[Vector([[1, 0, 0]]), Vector([[0, 1, 0]]), Vector([[0, 0, 1]])], self.matrix[0],
                        other.matrix[0]])
        return result.determinant()

    def length(self):
        return round(Matrix.norm(self), PRECISION)

    def dim(self):
        return [self.height, self.width]

    def __mod__(self, other):
        return Vector.scalar_product(self, other)

    def __pow__(self, other):
        return Vector.vector_product(self, other)


def BilinearForm(matrix: Matrix, vec1: Vector, vec2: Vector):
    if not (matrix.height == matrix.width and matrix.height == vec1.width and
            matrix.height == vec2.width):
        raise EngineException(MatrixException.MATRIX_WRONG_SIZES)

    result = 0
    for i in range(matrix.height):
        for j in range(matrix.height):
            result += matrix[i][j]*vec1[0][i]*vec2[0][i]
    return round(result, PRECISION)


class Point(Vector):
    def __init__(self, point):
        if isinstance(point, list):
            super().__init__(point)

    def addition(self, other: Vector):
        if isinstance(self, Point) and isinstance(other, Point):
            raise EngineException(PointException.POINT_TWO_INCORRECT)
        if not isinstance(other, Vector):
            raise EngineException(EngineException.WRONG_USAGE)
        if self.size != other.size:
            raise EngineException(VectorException.VECTOR_SIZE)

        return Point([round(self.matrix[0][i] + other.matrix[0][i], PRECISION) for i in range(self.size)])

    def subtraction(self, other: Vector):
        if isinstance(self, Point) and isinstance(other, Point):
            raise EngineException(PointException.POINT_TWO_INCORRECT)
        if not isinstance(other, Vector):
            raise EngineException(EngineException.WRONG_USAGE)
        if self.size != other.size:
            raise EngineException(VectorException.VECTOR_SIZE)

        return Point([round(self.matrix[0][i] - other.matrix[0][i], PRECISION) for i in range(self.size)])

    def __add__(self, other):
        return Point.addition(self, other)

    def __sub__(self, other):
        return Point.subtraction(self, other)


class VectorSpace:
    def __init__(self, basis: list[Vector]):
        self.basis = Matrix([i.matrix[0] for i in basis])
        if self.basis.determinant() == 0:
            raise EngineException(VectorSpaceException.VECTORSPACE_NOT_BASIS)
        self.size = len(basis)

    def __repr__(self):
        return str(self.basis).replace("],", "],\n")

    def scalar_product(self, vector1: Vector, vector2: Vector):
        result = vector1.transpose() * Matrix.gram(self.basis)*vector2
        return result

    def as_vector(self, point):
        if point.size != self.size:
            raise EngineException(VectorException.VECTOR_SIZE)
        result = list()
        for i in range(self.size):
            vector = self.basis[i] * point[0][i]
            result.append(vector)
        return Vector(result)


class CoordinateSystem:
    def __init__(self, point: Point, vectorspace: VectorSpace):
        self.Point = point
        self.Vectorspace = vectorspace
