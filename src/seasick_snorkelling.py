"""This is the module that tests the changing seas."""
from __future__ import division


def sea_sick(sea):
    """The function tells you if you'll be sick by how much the sea changes."""
    z = 0
    for i in range(1, len(sea)):
        if sea[i] != sea[i - 1]:
            z += 1
    if z > 0 and float(z / len(sea)) > .2:
        return "Throw Up"
    else:
        return "No Problem"
