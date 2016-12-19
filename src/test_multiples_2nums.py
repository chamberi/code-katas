"""This is the test module for the multiples 2nums module."""
import pytest

MULTIPLES_TABLE = [
    [2, 4, 40, [4, 8, 12, 16, 20, 24, 28, 32, 36]],
    [3, 4, 40, [12, 24, 36]],
    [7, 4, 80, [28, 56]],
    [7, 4, 20, []],
]


@pytest.mark.parametrize("s1, s2, s3, result", MULTIPLES_TABLE)
def test_multiples(s1, s2, s3, result):
    """Test that 2 nums are multiples of a 3rd num, not inclusive."""
    from multiples_2nums import multiples
    assert multiples(s1, s2, s3) == result
