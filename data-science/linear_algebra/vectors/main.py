import math

"""
    Abstractly, vectors are objects that can be added together to form new
    vectors and that can be multiplied by scalars (i.e., numbers), also to form
    new vectors.

    Concretely (for us), vectors are points in some finite-dimensional space.
    Although you might not think of your data as vectors, they are often a
    useful way to represent numeric data.
    For example, if you have the heights, weights, and ages of a large number
    of people, you can treat your data as three-dimensional vectors [height,
    weight, age]. If you’re teaching a class with four exams, you can treat
    student grades as four-dimensional vectors [exam1, exam2, exam3,
    exam4].
    The simplest from-scratch approach is to represent vectors as lists of
    numbers. A list of three numbers corresponds to a vector in three-dimensional space, and vice versa.
"""

from typing import List

Vector = List[float]

height_weight_age = [70,  # inches,
                     170,  # pounds,
                     40]  # years

grades = [95,  # exam1
          80,  # exam2
          75,  # exam3
          62]  # exam4

"""
    We’ll also want to perform arithmetic on vectors. Because Python lists
    aren’t vectors (and hence provide no facilities for vector arithmetic), we’ll
    need to build these arithmetic tools ourselves. So let’s start with that.
    
    To begin with, we’ll frequently need to add two vectors. Vectors add
    componentwise. This means that if two vectors v and w are the same length,
    their sum is just the vector whose first element is v[0] + w[0], whose
    second element is v[1] + w[1], and so on. (If they’re not the same length,
    then we’re not allowed to add them.)
    For example, adding the vectors [1, 2] and [2, 1] results in [1 + 2, 2
    + 1] or [3, 3],
"""


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


# Similarly, to subtract two vectors we just subtract the corresponding
# elements:

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""

    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

"""
    We’ll also need to be able to multiply a vector by a scalar, which we do
    simply by multiplying each element of the vector by that number:
"""


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

"""
    This allows us to compute the componentwise means of a list of (samesized) vectors:

"""


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


"""
    A less obvious tool is the dot product. The dot product of two vectors is the
    sum of their componentwise products:
"""


def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6

"""
    Using this, it’s easy to compute a vector’s sum of squares:
"""


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


"""
    When a vector starts from the origin (0,0), its components are equal to the coordinates of its terminal point (where it ends). In this case, you can calculate the magnitude by taking the square root of the sum of the squares of these components. For example, a vector [3,4] starting from the origin has magnitude:

    Magnitude = √(3^2 + 4^2) = √(9 + 16) = √25 = 5.
    This method is what you will see here implemented, but don't forget that it only works for vectors starting from the origin. 

    When a vector doesn't start from the origin and has an initial point (x₁, y₁) and a terminal point (x₂, y₂), you calculate its components (Δx and Δy) as the differences between the terminal and initial coordinates:

    Δx = x₂ - x₁
    Δy = y₂ - y₁

    You can then calculate the magnitude using these components:

    Magnitude = √(Δx^2 + Δy^2).
"""


# assuming that the vector starts from the origin
def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))  # math.sqrt is square root function


assert magnitude([3, 4]) == 5

"""
We now have all the pieces we need to compute the distance between two
vectors, defined as:
    dist(u,v) = || u - v || = √((u_1 - v_1)^2 + ... + (u_n - v_n)^2)
"""


# Therefore our distance is:

def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))


assert distance([7, 1], [3, 2]) == math.sqrt(17)
