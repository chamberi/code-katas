"""The test module for sum of nth terms. I added more tests than code wars showed."""
import pytest

FRACTION_TABLE = [
    [0, "0.00"],
    [1, "1.00"],
    [2, "1.25"],
    [3, "1.39"],
    [4, "1.49"],
    [5, "1.57"],
    [6, "1.63"],
]


@pytest.mark.parametrize("iterable, result", FRACTION_TABLE)
def test_proper_parenthetics(iterable, result):
    """Test different arguments of the sum of nth terms module."""
    from sum_of_nth_terms import series_sum
    assert series_sum(iterable) == result
