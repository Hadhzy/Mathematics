"""
    Through a combination of word of mouth and luck, DataSciencester has
    grown to dozens of members, and the VP of Fundraising asks you for some
    sort of description of how many friends your members have that he can
    include in his elevator pitches.

    But now you are faced with the problem of how to describe it.
    One obvious description of any dataset is simply the data itself.
"""

"""
    For a small enough dataset, this might even be the best description. But for
    a larger dataset, this is unwieldy and probably opaque. (Imagine staring at a
    list of 1 million numbers.) For that reason, we use statistics to distill and
    communicate relevant features of our data.
    
    As a first approach, you put the friend counts into a histogram using
    Counter and plt.bar
"""

from collections import Counter
import matplotlib.pyplot as plt

num_friends = [2, 3, 4]

friend_counts = Counter(num_friends)
xs = range(101)  # largest value is 100
ys = [friend_counts[x] for x in xs]  # height is just # of friends
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")

"""
    Unfortunately, this chart is still too difficult to slip into conversations. So
    you start generating some statistics. Probably the simplest statistic is the
    number of data points:
"""

num_points = len(num_friends)  # 204
largest_value = max(num_friends)  # 100
smallest_value = min(num_friends)  # 1

# But we’re only getting started.
