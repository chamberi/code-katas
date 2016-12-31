"""This module builds list of multiples from 2 nums up unto the 3d num."""


def multiples(s1, s2, s3):
    """The function determines how many times 2 nums are multiples of 3rd."""
    new_list = []
    for i in range(1, s3 - 1):
        if i % s1 == 0 and i % s2 == 0:
            new_list.append(i)
    return new_list
