from typing import List, Tuple, Callable

Vector = List[float]
"""
    A matrix is a two-dimensional collection of numbers. We will represent
    matrices as lists of lists, with each inner list having the same size and
    representing a row of the matrix. If A is a matrix, then A[i][j] is the
    element in the ith row and the jth column. Per mathematical convention, we
    will frequently use capital letters to represent matrices. For example:
"""

Matrix = List[List[float]]

A = [[1, 2, 3],  # A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2],  # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]

"""
    Given this list-of-lists representation, the matrix A has len(A) rows and
    len(A[0]) columns, which we consider its shape:
"""


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # number of elements in first row
    return num_rows, num_cols


"""
     If a matrix has n rows and k columns, we will refer to it as an n × k matrix.
     We can (and sometimes will) think of each row of an n × k matrix as a
     vector of length k, and each column as a vector of length n:
"""


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]  # A[i] is already the ith row


def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]  # jth element of row A_i
            for A_i in A]  # for each row A_i


"""
    We’ll also want to be able to create a matrix given its shape and a function
    for generating its elements. We can do this using a nested list
    comprehension:
"""


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)  # given i, create a list
             for j in range(num_cols)]  # [entry_fn(i, 0), ... ]
            for i in range(num_rows)]  # create one list for each i


"""
    Given this function, you could make a 5 × 5 identity matrix (with 1s on the
    diagonal and 0s elsewhere) like so:
"""


def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]
