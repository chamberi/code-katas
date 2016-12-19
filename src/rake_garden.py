"""This module removes non rock and gravel from the garden."""


def rake_garden(garden):
    """The function removes non gravel or rock from the garden, and replaces it with gravel."""
    list_garden = garden.split()
    for i, c in enumerate(list_garden):
        if list_garden[i] != "gravel" and list_garden[i] != "rock":
            list_garden[i] = "gravel"
    a = " ".join(list_garden)
    return a
