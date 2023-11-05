from matplotlib import pyplot as plt

"""
    A bar chart is a good choice when you want to show how some quantity
    varies among some discrete set of items.
     For instance, we can show
    how many Academy Awards were won by each of a variety of movies:
"""

# movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10]
#
# # plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
# plt.bar(range(len(movies)), num_oscars)
#
# plt.bar(range(len(movies)), num_oscars)
#
# plt.title("My Favorite Movies")  # add a title
#
# plt.ylabel("# of Academy Awards")  # label the y-axis
#
# # label x-axis with movie names at bar centers
# plt.xticks(range(len(movies)), movies)

# plt.show()

"""
    A bar chart can also be a good choice for plotting histograms of bucketed
    numeric values, in order to visually explore how the values
    are distributed:

"""
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90s

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

print(histogram)

plt.bar([x + 5 for x in histogram.keys()],  # Shift bars right by 5
        histogram.values(),  # Give each bar its correct height
        10,  # Give each bar a width of 10
        edgecolor=(0, 0, 0))  # Black edges for each bar

plt.axis([-5, 105, 0, 5])  # x-axis from -5 to 105, y-axis from 0 to 5

plt.xticks([10 * i for i in range(11)])  # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

"""
        The third argument to plt.bar specifies the bar width. Here we chose a
        width of 10, to fill the entire decile. We also shifted the bars right by 5, so
        that, for example, the “10” bar (which corresponds to the decile 10–20)
        would have its center at 15 and hence occupy the correct range. We also
        added a black edge to each bar to make them visually distinct.
        The call to plt.axis indicates that we want the x-axis to range from –5 to
        105 (just to leave a little space on the left and right), and that the y-axis
        should range from 0 to 5. And the call to plt.xticks puts x-axis labels at
        0, 10, 20, …, 100.
        Be judicious when using plt.axis. When creating bar charts it is
        considered especially bad form for your y-axis not to start at 0, since this is
        an easy way to mislead people.
"""