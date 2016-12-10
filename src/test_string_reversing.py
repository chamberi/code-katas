"""This is the test module for the string reversing module."""
import pytest

FIZZ_BUZZ_TABLE = [
    ["FizZ", "buZZ", "zzUB@@@zZIffIZz"],
    ["String Reversing", "Changing Case", "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING"],
]


@pytest.mark.parametrize("s1, s2, result", FIZZ_BUZZ_TABLE)
def test_fizz_buzz_cuckoo_clock(s1, s2, result):
    """Test reversing strings and changing cases on words."""
    from string_reversing import reverse_and_mirror
    assert reverse_and_mirror(s1, s2) == result
