from lib.math.main import *

if __name__ == "__main__":
    m = Matrix([[1, 2, 3, 19, 6], [0, 4, 4, 7, 8], [1, 21, 44, 41, 10], [1, 0, 1, 22, 22], [1, 2, 3, 4, 5]])
    print(m.determinant())
    v = Vector([1, 2, 3])
    v1 = Vector([[1], [2], [3]])
    print(v*v1)
    m1 = Matrix([[1, 2, 3], [3, 2, 1], [1, 2, 5]])
    m2 = Matrix([[4], [6], [8]])
    print(m2*m1)
    # y = Vector([-1, -2, -3])
    # print(x*y)
    # m = Matrix([[1,2,3,18],[0,3,4,7],[1,21,44,41],[1,0,1,22]])
    # print("\nPrinting m\n\n", m)
    # print("\nIdentity matrix of same size \n\n", Matrix.identity(m, 4))
    # print("\nAll one matrix \n\n", m.zero_matrix(2, 5))
    # print("\nCommon matrix and scalar operations \n\n", m*m+3*m-0.5*m-2)
    # print("\nDeterminant ", m.determinant())
    # print("\nTranspose \n\n", m.transpose())
    # i = m.inverse();
    # print("\nInverse \n\n", i)
    # m1 = Matrix([[1.0, 2.0], [3, 4]])
    # print("\nGram \n\n", m.gram())
    # v = Vector([1, 4, 6])
    # v2 = Vector([1, 5, 4])
    # print("\nVector scalar \n", Vector.scalar(v, v2))
    # print(v % v2)
    # vector = Vector([1, 2, 3])
    # v1 = Vector([1, 5, 7])
    # v2 = Vector([2, 4, 6])
    # print("\nVector transonse \n",Vector.transponse(vector))
    # print("\nVector vecor_product \n",Vector.vector_product(v1, v2))
    # print(v1 ** v2)
    # print("\nVector lenght \n", Vector.lenght(v2))
    # p = Point([1, 2, 3])
    # v = Vector([3, 4, 5])
    # print("\nPoint - Vector \n", p - v)
    # m1 = Matrix([[1, 2, 3], [4, 5, 6], [9, 8, 8]])
    # vector1 = Vector([1, 2, 3])
    # vector2 = Vector([1.8, 2.1, 4.5])
    # base = VectorSpace([[1, 0, 0 ], [0, 1, 0], [0, 0, 1]])
    # print("\n Scalar-product \n", VectorSpace.scalar_product(base, vector1, vector2))