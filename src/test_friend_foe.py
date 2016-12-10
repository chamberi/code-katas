"""This is the test module for the friend or foe module."""
import pytest

FRIEND_FOE_TABLE = [
    [["Ryan", "Kieran", "Mark"], ["Ryan", "Mark"]],
]


@pytest.mark.parametrize("flist, result", FRIEND_FOE_TABLE)
def test_friend(flist, result):
    """Test picking out friends with 4 letters in name."""
    from friend_foe import friend
    assert friend(flist) == result
