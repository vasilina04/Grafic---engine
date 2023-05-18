class EngineException (Exception):
    WRONG_USAGE = "The method is called by the wrong class"


class MatrixException (EngineException):
    MATRIX_UNKNOWN_OPERATION = "This operation isn ’t defined for matrix "
    MATRIX_WRONG_SIZES = "The matrix is of the wrong size"
    MATRIX_NOT_SQUARE = "The matrix is not square"
    MATRIX_INCORRECT = "The number of elements in different rows are different"
    MATRIX_EMPTY = "The matrix does not contain elements"
    GRAM_LIST_ERROR = "The list does not contain vectors"
    GRAM_DIFFERENT_SIZE = "Vectors of different sizes"


class VectorException (EngineException):
    VECTOR_UNKNOWN_OPERATION = "This operation isn ’t defined for vector"
    VECTOR_SIZE = "The vector is of the wrong size"
    VECTOR_VECTOR_PRODUCT = "Vector size isn't 3"
    VECTOR_BASIS = "Vector and basis dimension mismatch"


class PointException (EngineException):
    POINT_TWO_INCORRECT = "The action with two points is not possible"
    POINT_EMPTY = "The point does not contain elements"


class VectorSpaceException (EngineException):
    VECTORSPACE_NOT_BASIS = "This is not a basis"