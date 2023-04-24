from main import *
import pytest
import math


class TestMatrix:
    def testInititialitation(self):
        m = Matrix([[1, 2], [3, 4]])

        act = isinstance(m, Matrix)

        assert act

    def testSize(self):
        m = Matrix([[1, 2, 3]])

        act = (m.width == 3 and m.height == 1)

        assert act

    def testZeroMatrixSize(self):
        zero = Matrix.zero_matrix(2, 5)

        act = (zero.width == 2 and zero.height == 5)

        assert act

    def testZeroMatrix(self):
        zero = Matrix.zero_matrix(2, 3)
        m = Matrix([[0, 0], [0, 0], [0, 0]])

        act = (m == zero)
        assert act

    def testIdentity(self):
        n = 2
        m1 = Matrix([[1, 0], [0, 1]])

        act = (Matrix.identity(n) == m1)

        assert act

    def testSum(self):
        m = Matrix([[1, 2], [5, 6]])
        m1 = Matrix([[1, 4], [2, 8]])
        m2 = Matrix([[2, 6], [7, 14]])

        act = (m + m1 == m2)

        assert act

    def testDifferent(self):
        m = Matrix([[4, 5], [3, 6]])
        m1 = Matrix([[1, 4], [2, 8]])
        m2 = Matrix([[3, 1], [1, -2]])

        act = (m - m1 == m2)

        assert act

    def testMul(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[7, 8], [9, 10], [11, 12]])
        m = Matrix([[58, 64], [139, 154]])

        act = (m1 * m2 == m)

        assert act

    def testDeterminant(self):
        m = Matrix([[1, 2, 3, 18], [0, 3, 4, 7], [1, 21, 44, 41], [1, 0, 1, 22]])
        det = 450

        act = (det == Matrix.determinant(m))

        assert act

    def testTransponse(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[1, 4], [2, 5], [3, 6]])

        act = (m2 == Matrix.transpose(m1))

        assert act

    def testgetmatrixMinor(self):
        m1 = Matrix([[1, 2, 3, 18], [0, 3, 4, 7], [1, 21, 44, 41], [1, 0, 1, 22]])
        m2 = Matrix([[3, 4, 7], [21, 44, 41], [0, 1, 22]])

        act = (m2 == Matrix.get_matrix_minor(m1, 0))

        assert act

    def testInverse(self):
        m = Matrix([[1, 2], [3, 4]])
        m1 = Matrix([[-2.0, 1.0], [1.5, -0.5]])

        act = (m1 == Matrix.inverse(m))

        assert act

    def testRotate(self):
        m = Matrix([[1, 2], [3, 4]])

        act = (m.rotate_matrix(m, 0, 1, math.pi/2) == Matrix([[-2, 1], [-4, 3]]))

        assert act


