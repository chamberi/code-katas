"""This is the module for summing up numbers within a random string."""
import re


def sum_from_string(string):
    """The function sums up the numbers in a string."""
    if any(i.isdigit() for i in string):
        z = re.findall('\d+', string)
        a = map(int, z)
        b = sum(a)
        return b
    else:
        return 0
