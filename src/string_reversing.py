"""This is the module to reverse the order of letters and change case on words."""


def reverse_and_mirror(s1, s2):
    """Convert words to switch case and reverse order."""
    news2 = []
    for x in s2[::-1]:
        news2.append(x.swapcase())
    news2.append("@@@")
    for y in s1[::-1]:
        news2.append(y.swapcase())
    for z in s1:
        news2.append(z.swapcase())
    a = map(str, news2)
    b = "".join(a)
    return b
