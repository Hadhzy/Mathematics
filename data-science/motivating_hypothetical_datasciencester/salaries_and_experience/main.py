from collections import defaultdict

"""
    Right as you’re about to head to lunch, the VP of Public Relations asks if
    you can provide some fun facts about how much data scientists earn. Salary
    data is of course sensitive, but he manages to provide you an anonymous
    dataset containing each user’s salary (in dollars) and tenure as a data
    scientist (in years):
"""

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)
                        ]

"""
    It seems clear that people with more experience tend to earn more. How can
    you turn this into a fun fact? Your first idea is to look at the average salary
    for each tenure:
"""

# Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)
#
# for salary, tenure in salaries_and_tenures:
#     salary_by_tenure[tenure].append(salary)

"""
    Let's bucket the tenures
"""


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# Then we can group together the salaries corresponding to each bucket:

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure[bucket].append(salary)

# And finally compute the average salary for each group:

# Keys are tenure buckets, values are average salary for that bucket.
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure.items()
}

print(average_salary_by_bucket)

"""
    And you have your soundbite: “Data scientists with more than five years’
    experience earn 65% more than data scientists with little or no experience!”
"""

"""
    But we chose the buckets in a pretty arbitrary way. What we’d really like is
    to make some statement about the salary effect—on average—of having an
    additional year of experience. In addition to making for a snappier fun fact,
    this allows us to make predictions about salaries that we don’t know. We’ll
    explore this idea later.
"""

"""
    It is very important to be aware and keep using the assert keyword.
    It is a good
    practice, and I strongly encourage you to make liberal use of it in your own
    code. (If you look at the book’s code on GitHub, you will see that it
    contains many, many more assert statements than are printed in the book.
    This helps me be confident that the code I’ve written for you is correct.)
"""

x = 1
assert x > 0, "x is not positive"

"""
    Often we will need to zip two or more iterables together. The zip function
    transforms multiple iterables into a single iterable of tuples of
    corresponding function:
"""

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# [pair for pair in zip(list1, list2)]
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(list(zip(*pairs)))  # unzip
