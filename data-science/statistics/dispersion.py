from typing import List
from describing_a_single_set_of_data import num_friends
from central_tendencies_second import median, mean, quantile
import math

"""
    Dispersion refers to measures of how spread out our data is. Typically
    they’re statistics for which values near zero signify not spread out at all and
    for which large values (whatever that means) signify very spread out. For
    instance, a very simple measure is the range, which is just the difference
    between the largest and smallest elements:
"""


def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


"""
    The range is zero precisely when the max and min are equal, which can only
    happen if the elements of x are all the same, which means the data is as
    dispersed as possible. Conversely, if the range is large, then the max is
    much larger than the min and the data is more spread out.
    Like the median, the range doesn’t really depend on the whole dataset. A
    dataset whose points are all either 0 or 100 has the same range as a dataset
    whose values are 0, 100, and lots of 50s. But it seems like the first dataset
    “should” be more spread out.
    
    Like the median, the range doesn’t really depend on the whole dataset. A
    dataset whose points are all either 0 or 100 has the same range as a dataset
    whose values are 0, 100, and lots of 50s. But it seems like the first dataset
    “should” be more spread out.
"""


def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def _sum_of_squares(xs: List[float]) -> float:
    """Return sum of squares of elements in xs"""
    return sum(x ** 2 for x in xs)


def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return _sum_of_squares(deviations) / (n - 1)


assert variance(num_friends) == 1

"""
    Now, whatever units our data is in (e.g., “friends”), all of our measures of
    central tendency are in that same unit. The range will similarly be in that
    same unit. The variance, on the other hand, has units that are the square of
    the original units (e.g., “friends squared”). As it can be hard to make sense
    of these, we often look instead at the standard deviation:
"""


def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))


"""
    Both the range and the standard deviation have the same outlier problem
    that we saw earlier for the mean. Using the same example, if our friendliest
    user had instead 200 friends, the standard deviation would be 14.89—more
    than 60% higher!
    A more robust alternative computes the difference between the 75th
    percentile value and the 25th percentile value:
"""


def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    print("quantile(xs, 0.75)", quantile(xs, 0.75))
    print("quantile(xs, 0.25", quantile(xs, 0.25))
    return quantile(xs, 0.75) - quantile(xs, 0.25)

# which is quite plainly unaffected by a small number of outliers.

# ------------
# Correlation
# ------------
