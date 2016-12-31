"""This tests the parenthetics module."""
import pytest

PAREN_TABLE = [
    [-1, "())(()"],
    [0, "()()()"],
    [-1, ")(()()"],
    [-1, "()())("],
    [1, "(((()))"],
    [-1, "(((()))))"],
    [1, "("],
    [-1, ")"],
    [0, "shrsljfguugsb"],
]


@pytest.mark.parametrize("result, iterable", PAREN_TABLE)
def test_proper_parenthetics(result, iterable):
    """Test different strings against the parenthetics module."""
    from parenthetics import proper_parenthetics
    assert proper_parenthetics(iterable) == result
