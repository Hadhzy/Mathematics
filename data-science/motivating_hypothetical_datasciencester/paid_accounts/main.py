"""
    When you get back to your desk, the VP of Revenue is waiting for you. She
    wants to better understand which users pay for accounts and which don’t.
    (She knows their names, but that’s not particularly actionable information.)
    You notice that there seems to be a correspondence between years of
    experience and paid accounts:

    0.7 paid
    1.9 unpaid
    2.5 paid
    4.2 unpaid
    6.0 unpaid
    6.5 unpaid
    7.5 unpaid
    8.1 unpaid
    8.7 paid
    10.0 paid

    Users with very few and very many years of experience tend to pay; users
    with average amounts of experience don’t. Accordingly, if you wanted to
    create a model—though this is definitely not enough data to base a model
    on—you might try to predict “paid” for users with very few and very many
    years of experience, and “unpaid” for users with middling amounts of
    experience:
"""


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


"""
    Of course, we totally eyeballed the cutoffs.
    With more data (and more mathematics), we could build a model predicting
    the likelihood that a user would pay based on his years of experience. We’ll
    investigate this sort of problem later.
"""

# Section: Topics of interest

"""
    As you’re wrapping up your first day, the VP of Content Strategy asks you
    for data about what topics users are most interested in, so that she can plan
    out her blog calendar accordingly. You already have the raw data from the
    friend-suggester project:
"""

from data_scientists_you_may_know.main import interests
from collections import Counter

"""
    One simple (if not particularly exciting) way to find the most popular
    interests is to count the words:
        1. Lowercase each interest (since different users may or may not
        capitalize their interests).
        2. Split it into words.
        3. Count the results.
"""

words_and_counts = Counter(word for user, interest in interests for word in interest.lower().split())

# This makes it easy to list out the words that occur more than once:

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)

"""
    It’s been a successful first day! Exhausted, you slip out of the building
    before anyone can ask you for anything else. Get a good night’s rest,
    because tomorrow is new employee orientation. (Yes, you went through a
    full day of work before new employee orientation. Take it up with HR.)
"""