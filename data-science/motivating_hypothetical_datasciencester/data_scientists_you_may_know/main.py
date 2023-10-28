from finding_key_connectors.main import *

# Section: Data Scientists You May Know

"""
    While you’re still filling out new-hire paperwork, the VP of Fraternization
    comes by your desk. She wants to encourage more connections among your
    members, and she asks you to design a “Data Scientists You May Know”
    suggester.
    Your first instinct is to suggest that users might know the friends of their
    friends. So you write some code to iterate over their friends and collect the
    friends’ friends:
"""


def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    result = []
    for friend_id in friendships[user["id"]]:
        for foaf_id in friendships[friend_id]:
            result.append(foaf_id)
    return result


# When we call this on users[0] (Hero), it produces:
foaf_ids_bad(users[0])  # [0, 2, 3, 0, 1, 3]

"""
    Knowing that people are friends of friends in multiple ways seems like
    interesting information, so maybe instead we should produce a count of
    mutual friends. And we should probably exclude people already known to
    the user:  
"""

from collections import Counter  # not loaded by default


def friends_of_friends(user):
    user_id = user["id"]
    return Counter([
        foaf_id
        for friend_id in friendships[user_id]  # for each of my friends,
        for foaf_id in friendships[friend_id]  # find their friends
        if foaf_id != user_id  # who aren't me
           and foaf_id not in friendships[user_id]  # and aren't my friends
    ])


friends_of_friends(users[0])

"""
    As a data scientist, you know that you also might enjoy meeting users with
    similar interests. (This is a good example of the “substantive expertise”
    aspect of data science.) After asking around, you manage to get your hands
    on this data, as a list of pairs (user_id, interest):
"""

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# For example, Hero (id 0) has no friends in common with Klein (id 9), but
# they share interests in Java and big data.
# It’s easy to build a function that finds users with a certain interest:


# def data_scientists_who_like(target_interest):
#     """Find the ids of all users who like the target interest."""
#     return [user_id
#             for user_id, user_interest in interests
#             if user_interest == target_interest]

"""
    This works, but it has to examine the whole list of interests for every
    search. If we have a lot of users and interests (or if we just want to do a lot
    of searches), we’re probably better off building an index from interests to
    users:
"""

from collections import defaultdict

# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Keys are user_ids, values are lists of interests in that user_id.
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

"""
    Now it’s easy to find who has the most interests in common with a given
    user:
    - Iterate over the user’s interests.
    - For each interest, iterate over the other users with that interest.
    - Keep count of how many times we see each other user.
"""


def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for _interest in interests_by_user_id[user["id"]] # find interests of user
        for interested_user_id in user_ids_by_interest[_interest] # find users with that interest
        if interested_user_id != user["id"] # exclude user
    )

"""
    We could then use this to build a richer “Data Scientists You May Know”
    feature based on a combination of mutual friends and mutual interests.
    We will explore these later.
"""