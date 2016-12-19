"""This is the test module that for removing nested lists from a big list."""
import pytest

FLATTEN_ME_TABLE = [
    [[1, [2, 3], 4], [1, 2, 3, 4]],
    [[['a', 'b'], 'c', ['d']], ['a', 'b', 'c', 'd']],
    [['!', '?'], ['!', '?']],
    [[[True, False], ['!'], ['?'], [71, '@']], [True, False, '!', '?', 71, '@']],
]


@pytest.mark.parametrize("nested, result", FLATTEN_ME_TABLE)
def flatten_me(nested, result):
    """Test flatten me, removing nested lists from big list."""
    from flatten_me import flatten_me
    assert flatten_me(nested) == result
