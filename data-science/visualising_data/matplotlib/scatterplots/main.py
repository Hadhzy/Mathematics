from matplotlib import pyplot as plt


"""
    A scatterplot is the right choice for visualizing the relationship between two
    paired sets of data. For example, The next figure illustrates the relationship
    between the number of friends your users have and the number of minutes
    they spend on the site every day.
"""

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, xy=(friend_count, minute_count), # Put the label with its point
        xytext=(5, -5), # but slightly offset
        textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")


plt.show()

"""
    If you’re scattering comparable variables, you might get a misleading
    picture if you let matplotlib choose the scale
    
    The matplotlib Gallery will give you a good idea of the sorts of
    things you can do with matplotlib (and how to do them).
    seaborn is built on top of matplotlib and allows you to easily
    produce prettier (and more complex) visualizations.
    Altair is a newer Python library for creating declarative
    visualizations.
    D3.js is a JavaScript library for producing sophisticated interactive
    visualizations for the web. Although it is not in Python, it is widely
    used, and it is well worth your while to be familiar with it.
    Bokeh is a library that brings D3-style visualizations into Python.
"""
