"""This module selects friends with 4 letters in their name."""


def friend(x):
    """Build list of friends with 4 letters."""
    friend_list = []
    for i, c in enumerate(x):
        if len(x[i]) == 4:
            friend_list.append(x[i])
    return friend_list
