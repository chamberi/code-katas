"""This is the test module for the sum up module."""
import pytest

SUM_STRING_TABLE = [
    ["In 2015, I want to know how much does iPhone 6+ cost?", 2021],
    ["1+1=2", 4],
    ["e=mc^2", 2],
]


@pytest.mark.parametrize("phrase, result", SUM_STRING_TABLE)
def test_sum_from_string(phrase, result):
    """Test summing up numbers from within a string."""
    from sum_up import sum_from_string
    assert sum_from_string(phrase) == result
