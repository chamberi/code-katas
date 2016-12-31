"""The module for sum of nth terms code kata, adding up the fractions in the series."""


def series_sum(listed):
    """The funcion adds the fractions together, returning the string representation a float with 2 precision points."""
    added = 0
    for i in range(listed):
        added += 1.0 / (1 + i * 3)
    return "{0:.2f}".format(added)
