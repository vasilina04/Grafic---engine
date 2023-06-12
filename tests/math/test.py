from lib.math.main import *
import pytest


class TestMatrix:
    def testInititialitation(self):
        m = Matrix([[1, 2], [3, 4]])

        act = isinstance(m, Matrix)

        assert act

    def testWrongMatrix1(self):

        with pytest.raises(EngineException):
            act = Matrix([[]])

    def testWrongMatrix(self):

        with pytest.raises(EngineException):

            act = Matrix([[1, 2], [3]])

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

    def testnormatrix(self):
        m = Matrix([[1, 2, 3]])
        m1 = 14**0.5

        act = (m.norm() == m1)

        assert act

    def test_transposition(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

        act = (m1.transpose() == m2)

        assert act

    def testSum(self):
        m = Matrix([[1, 2], [5, 6]])
        m1 = Matrix([[1, 4], [2, 8]])
        m2 = Matrix([[2, 6], [7, 14]])

        act = (Matrix.addition(m, m1) == m2)

        assert act

    def testCommutativeSum(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[2, 3], [1, 0]])

        act = (m1 + m2 == m2 + m1)

        assert act

    def testSumTransponse(self):
        m1 = Matrix([[1, 2], [3, 4]]).transpose()
        m2 = Matrix([[2, 3], [1, 0]]).transpose()

        act = (m1 + m2 == m2 + m1)

        assert act

    def testSumExceptionWrongSize(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2, 3], [2, 3, 1], [5, 1, 0]])

        with pytest.raises(EngineException):
            act = m1 + m2

    def testSumExeptionWrong(self):
        m = Matrix([[1, 2], [3, 4]])

        with pytest.raises(EngineException):
            act = m + 3

    def testSubtraction(self):
        m = Matrix([[4, 5], [3, 6]])
        m1 = Matrix([[1, 4], [2, 8]])
        m2 = Matrix([[3, 1], [1, -2]])

        act = (m - m1 == m2)

        assert act

    def testSubExceptionWrongSize(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2, 3], [2, 3, 1], [5, 1, 0]])

        with pytest.raises(EngineException):
            act = m1 - m2

    def testSubExeptionWrong1(self):
        m = Matrix([[1, 2], [3, 4]])

        with pytest.raises(EngineException):
            act = m - 3

    def testSubtraction1(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
        m3 = Matrix([[9, 9, 9], [9, 9, 9], [9, 9, 9]])

        act = (m2 - m1 == m3)

        assert act

    def testMul(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[7, 8], [9, 10], [11, 12]])
        m = Matrix([[58, 64], [139, 154]])

        act = (m1 * m2 == m)

        assert act

    def testMultiplication1(self):
        m1 = Matrix([[1, 2, 3], [3, 2, 1]])
        m2 = Matrix([[4, 5], [6, 7], [8, 9]])
        m3 = Matrix([[40, 46], [32, 38]])

        act = (m1 * m2 == m3)

        assert act

    def testMultiplication2(self):
        m1 = Matrix([[1, 2, 3], [3, 2, 1], [1, 2, 5]])
        m2 = Matrix([[4], [6], [8]])
        m3 = Matrix([[4, 8, 12], [6, 12, 18], [8, 16, 24]])

        act = (m2 * m1 == m3)

        assert act

    def testDeterminant(self):
        m = Matrix([[1, 2, 3, 18], [0, 3, 4, 7], [1, 21, 44, 41], [1, 0, 1, 22]])
        det = 450

        act = (det == Matrix.determinant(m))

        assert act

    def testDeterminant1(self):
        m = Matrix([[1, 2, 3, 19, 6], [0, 4, 4, 7, 8], [1, 21, 44, 41, 10], [1, 0, 1, 22, 22], [1, 2, 3, 4, 5]])
        det = 25828

        act = (det == Matrix.determinant(m))

        assert act

    def testDeterminantWrong(self):
        m = Matrix([[1, 2, 3, 18], [1, 21, 44, 41], [1, 0, 1, 22]])

        with pytest.raises(EngineException):
            act = m.determinant()

    def testTransponse(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 3], [2, 4]])

        act = (m2 == m1.transpose())

        assert act

    def testgetmatrixMinor(self):
        m1 = Matrix([[1, 2, 3, 18], [0, 3, 4, 7], [1, 21, 44, 41], [1, 0, 1, 22]])
        m2 = Matrix([[3, 4, 7], [21, 44, 41], [0, 1, 22]])

        act = (m2 == Matrix.get_matrix_minor(m1, 0))

        assert act

    def testinverse(self):
        m = Matrix([[1, 2], [3, 4]])
        m1 = Matrix([[-2.0, 1.0], [1.5, -0.5]])

        act = (Matrix(m.inverse()) == m1)

        return act

    def testGram(self):
        m = Matrix([[1, 2], [3, 4]])

        act = (m.gram() == Matrix([[5, 11], [11, 25]]))

        assert act

    def testRotator(self):
        m1 = Matrix.rotate_matrix(3, 0, 1, 45)
        m2 = Matrix([[0.7071067811865476, -0.7071067811865476, 0],
                     [0.7071067811865476, 0.7071067811865476, 0],
                     [0, 0, 1]])

        assert m1 == m2

    def testRotatesizeError(self):

        with pytest.raises(EngineException):
            Matrix.rotate_matrix(0.5, 0, 1, 56)

    def testRotateindexError(self):

        with pytest.raises(EngineException):
            Matrix.rotate_matrix(90, 0, 6.9, 1)

    def testInverseWrong(self):
        v = Vector([1, 2, 3])

        with pytest.raises(EngineException):
            Matrix.inverse(v)


class TestVector:
    def testVectorInitial(self):
        v = Vector([1, 2, 3])

        act = isinstance(v, Vector)

        assert act

    def testVectorInitial_row(self):
        v = Vector([[1], [2], [3]])

        act = isinstance(v, Vector)

        assert act

    def testVectorInitial_null(self):
        v = Vector(2)
        result = Vector([[0, 0]])

        act = (v == result)

        assert act

    def testTranspose(self):
        v = Vector([1, 2, 3])
        v1 = Vector([[1], [2], [3]])

        act = (v.transpose() == v1)

        assert act

    def testLengthvector(self):
        v = Vector([1, 2, 3])
        res = 14**0.5

        act = (v.length() == res)

        assert act

    def testVectorMultiplication(self):
        v = Vector([1, 2, 3])
        v1 = Vector([[1], [2], [3]])

        act = isinstance(v*v1, Vector)

        assert act

    def testscalarProduct_Vector(self):
        v = Vector([1, 3, 5])
        v1 = Vector([2, 4, 5])
        res = 39

        act = (v % v1 == res)

        assert act

    def testscalar_product_Vector_fun(self):
        v = Vector([1, 3, 5])
        v1 = Vector([2, 4, 5])
        res = 39

        act = (Vector.scalar_product(v, v1) == res)

        assert act

    def testscalarVectorWrong(self):
        v = Vector([1, 3, 5])
        v1 = Vector([2, 4])

        with pytest.raises(EngineException):
            act = (v % v1)

    def testVectorProduct(self):
        v = Vector([8, 2, 5])
        v1 = Vector([4, 6, 7])
        result = Vector([-16, -36, 40])

        act = (v ** v1 == result)

        assert act

    def testVectorProductTransdifferent(self):
        v = Vector([8, 2, 5])
        v1 = Vector([4, 6, 7]).transpose()
        result = Vector([-16, -36, 40])

        act = (v ** v1 == result)

        assert act

    def testVectorProduct_func(self):
        v = Vector([8, 2, 5])
        v1 = Vector([4, 6, 7])
        result = Vector([-16, -36, 40])

        act = (Vector.vector_product(v, v1) == result)

        assert act

    def testVectornormalize(self):
        v = Vector([1, 2, 3])
        norma = 14**0.5
        result = Vector([[1/norma, 2/norma, 3/norma]])

        act = (v.normalize() == result)

        assert act

    def testVectorProductException(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 4, 5])

        with pytest.raises(EngineException):
            act = v1 * v2

    def testMultiplyWithScalar(self):
        v1 = Vector([1, 2, 3])

        act = v1 * 2 == Vector([2, 4, 6])

        assert act

    def testMultiplyWithVector(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([[1], [2], [4]])

        act = v1 * v2 == Vector([17])

        assert act

    def testDim(self):
        v = Vector([1, 3, 4])

        act = (v.dim() == [1, 3])

        assert act

    def testDim2(self):
        v = Vector([[1], [3], [4]])

        act = (v.dim() == [3, 1])

        assert act

    def testSubtractionHorizontal(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 4])

        act = v2 - v1 == Vector([0, 0, 1])

        assert act

    def testLength(self):
        v = Vector([1, 3, 4])
        res = 26**0.5

        act = (v.length() == res)

        assert act

    def testSumVectorIsitanse(self):
        v = Vector([1, 2, 3])
        v1 = Vector([[1], [2], [3]])

        act = isinstance(v1*v, Vector)

        assert act

    def testWrongVector1(self):
        with pytest.raises(EngineException):
            act = Vector([[]])


class TestPoint:
    def testInititialitation(self):
        p = Point([1, 2])

        act = isinstance(p, Point)

        assert act

    def testSumPointVector(self):
        v = Vector([1, 2, 3])
        p = Point([1, 2, 3])
        p_new = Point([2, 4, 6])

        act = (p + v == p_new)

        assert act

    def testSubPointVector(self):
        v = Vector([1, 2, 3])
        p = Point([1, 2, 3])
        p_new = Point([0, 0, 0])

        act = (p - v == p_new)

        assert act

    def testSubPointVectortype(self):
        v = Vector([1, 2, 3])
        p = Point([1, 2, 3])
        p_new = Point([0, 0, 0])

        act = isinstance(p - v, Point)

        assert act

    def testSumWrong(self):
        p = Point([[1, 2]])
        p1 = Point([1, 5])

        with pytest.raises(EngineException):
            act = p+p1

    def testSumWrong_size(self):
        p = Point([[1, 2]])
        v = Vector([1, 5, 8])

        with pytest.raises(EngineException):
            act = p+v

    def testSubWrong(self):
        p = Point([[1, 2]])
        p1 = Point([1, 5])

        with pytest.raises(EngineException):
            act = p-p1

    def testSubWrong_size(self):
        p = Point([[1, 2]])
        v = Vector([1, 5, 8])

        with pytest.raises(EngineException):
            act = p-v


class TestVectorSpace:
    def testInitialitationVectorSpace(self):
        base = VectorSpace([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])

        act = isinstance(base, VectorSpace)

        assert act


class TestCoordinateSystem:
    def testInitializationCoordinateSystem(self):
        p = Point([1, 2, 3])
        vs = VectorSpace([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])
        Coordinatesystem = CoordinateSystem(p, vs)

        act = isinstance(Coordinatesystem, CoordinateSystem)

        assert act


class TestBilinearForm:
    def testBilinearform(self):
        vec1 = Vector([[3, 7, 1]])
        vec2 = Vector([[0, 2, 5]])
        m = Matrix([[3, 6, 1],
                    [9, 0, 3],
                    [0, 5, 1]])
        act = BilinearForm(m, vec1, vec2) == 198

        assert act








