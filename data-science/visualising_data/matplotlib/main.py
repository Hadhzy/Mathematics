"""
    A wide variety of tools exist for visualizing data. We will be using the
    matplotlib library, which is widely used (although sort of showing its age).
    If you are interested in producing elaborate interactive visualizations for the
    web, it is likely not the right choice, but for simple bar charts, line charts,
    and scatter plots, it works pretty well.
"""

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]


# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# add a title
plt.title("Nominal GDP")

# add a label to the y-axis
plt.ylabel("Billions of $")

# plt.show()

"""
    Making plots that look publication-quality good is more complicated and
    beyond the scope of this chapter. There are many ways you can customize
    your charts with, for example, axis labels, line styles, and point markers.
    Rather than attempt a comprehensive treatment of these options, we’ll just
    use (and call attention to) some of them in our examples.
"""
