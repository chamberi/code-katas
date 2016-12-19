"""We remove nested lists within a larger list of lists."""


def flatten_me(lst):
    """Remove nested lists from within a bigger list."""
    b = []
    for sublist in lst:
        if type(sublist) is not list:
            b.append(sublist)
        else:
            for next_sub in sublist:
                b.append(next_sub)
    return b
