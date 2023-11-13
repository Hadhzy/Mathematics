from describing_a_single_set_of_data import num_friends

"""
    Usually, we’ll want some notion of where our data is centered. Most
    commonly we’ll use the mean (or average), which is just the sum of the
    data divided by its count:
"""
from typing import List
from collections import Counter


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


mean(num_friends)  # 7.333333

"""
    If you have two data points, the mean is simply the point halfway between
    them. As you add more points, the mean shifts around, but it always
    depends on the value of every point. For example, if you have 10 data
    points, and you increase the value of any of them by 1, you increase the
    mean by 0.1.
    We’ll also sometimes be interested in the median, which is the middle-most
    value (if the number of data points is odd) or the average of the two middlemost values (if the number of data points is even).
    For instance, if we have five data points in a sorted vector x, the median is
    x[5 // 2] or x[2]. If we have six data points, we want the average of
    x[2] (the third point) and x[3] (the fourth point).
    Notice that—unlike the mean—the median doesn’t fully depend on every
    value in your data. For example, if you make the largest point larger (or the
    smallest point smaller), the middle points remain unchanged, which means
    so does the median.
"""


# We’ll write different functions for the even and odd cases and combine
# them:
# The underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library.

def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(v: List[float]) -> float:
    """"Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

"""
    And now we can compute the median number of friends:
"""

# print(median(num_friends))  # 15

"""
    Clearly, the mean is simpler to compute, and it varies smoothly as our data
    changes. If we have n data points and one of them increases by some small
    amount e, then necessarily the mean will increase by e / n. (This makes the
    mean amenable to all sorts of calculus tricks.) In order to find the median,
    however, we have to sort our data. And changing one of our data points by a
    small amount e might increase the median by e, by some number less than
    e, or not at all (depending on the rest of the data).
    
    At the same time, the mean is very sensitive to outliers in our data. If our
    friendliest user had 200 friends (instead of 100), then the mean would rise
    to 7.82, while the median would stay the same. If outliers are likely to be
    bad data (or otherwise unrepresentative of whatever phenomenon we’re
    trying to understand), then the mean can sometimes give us a misleading
    picture. For example, the story is often told that in the mid-1980s, the major
    at the University of North Carolina with the highest average starting salary
    was geography, mostly because of NBA star (and outlier) Michael Jordan.
    A generalization of the median is the quantile, which represents the value
    under which a certain percentile of the data lies (the median represents the
    value under which 50% of the data lies):
    
    A percentile is a way to measure where a particular data point stands in relation to a larger dataset. 
    It tells you what percentage of the data is below or equal to a given value. 
    For example, the 25th percentile (commonly called the first quartile) is the value below which 25% of the data falls.
    For example if we have a list of 8 values, then the 10th percentile is calculated as:
    8 * (10 / 100) = 0.8
"""


def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


data = [12.5, 3.2, 8.7, 5.1, 1.6, 9.8, 6.4, 2.2]
assert quantile(data, 0.10) == 1.6


# Less commonly you might want to look at the mode, or most common
# value(s):

def mode(x: List[float]) -> List[float]:
    """Returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


print(set(mode(num_friends)))
