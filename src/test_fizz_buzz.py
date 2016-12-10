"""This is the test module for the Fizz Buzz module."""
import pytest

FIZZ_BUZZ_TABLE = [
    ["13:34", "tick"],
    ["21:00", "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"],
    ["11:15", "Fizz Buzz"],
    ["03:03", "Fizz"],
    ["14:30", "Cuckoo"],
    ["08:55", "Buzz"]
]


@pytest.mark.parametrize("time, result", FIZZ_BUZZ_TABLE)
def test_fizz_buzz_cuckoo_clock(time, result):
    """Test cuckoo clock says the correct thing at a certain time."""
    from fizz_buzz import fizz_buzz_cuckoo_clock
    assert fizz_buzz_cuckoo_clock(time) == result
