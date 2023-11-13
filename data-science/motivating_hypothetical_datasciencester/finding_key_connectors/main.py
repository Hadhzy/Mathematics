"""
    Congratulations! You’ve just been hired to lead the data science efforts at
    DataSciencester, the social network for data scientists.
    It’s your first day on the job at DataSciencester, and the VP of Networking
    is full of questions about your users. Until now he’s had no one to ask, so
    he’s very excited to have you aboard. In particular, he wants you to identify who the “key connectors” are among
    data scientists. To this end, he gives you a dump of the entire
    DataSciencester network. What does this data dump look like? It consists of a list of users, each
    represented by a dict that contains that user’s id (which is a number) and
    name (which, in one of the great cosmic coincidences, rhymes with the
    user’s id):
"""
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

# He also gives you the “friendship” data, represented as a list of pairs of IDs:
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# For example, the tuple (0, 1) indicates that the data scientist with id 0 (Hero) and the data scientist with id 1 (Dunn) are friends.

"""
 To find all the friendships for user 1, you have to iterate
over every pair looking for pairs containing 1. If you had a lot of pairs, this
would take a long time.
"""

# let’s create a dict where the keys are user ids and the values are lists of friend ids. (Looking things up in a dict is very fast.)
# We’ll still have to look at every pair to create the dict, but we only have to do that once, and we’ll get cheap lookups after that:

# Initialize the dict with an empty list for each user id:
# {user_id: []...}
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

"""
Now that we have the friendships in a dict, we can easily ask questions of
our graph, like “What’s the average number of connections?”
"""

"""
First we find the total number of connections, by summing up the lengths of
all the friends lists:
"""


def number_of_friends(user):
    """how many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user) for user in users)  # 24
num_users = len(users)  # length of the users list
avg_connections = total_connections / num_users  # 2.4

"""
It’s also easy to find the most connected people—they’re the people who
have the largest numbers of friends. Since there aren’t very many users, we can simply sort them from “most
friends” to “least friends”:
"""

# Create a list (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],  # by num_friends
    reverse=True  # largest to smallest
)


# Each pair is (user_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

"""
    One way to think of what we’ve done is as a way of identifying people who
    are somehow central to the network. In fact, what we’ve just computed is
    the network metric degree centrality. See picture: network_sized_by_degree_based_on_id.png
    
    This has the virtue of being pretty easy to calculate, but it doesn’t always
    give the results you’d want or expect. For example, in the DataSciencester
    network Thor (id 4) only has two connections, while Dunn (id 1) has three.
    Yet when we look at the network, it intuitively seems like Thor should be
    more central.
"""
# ---

