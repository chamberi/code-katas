"""This is the test module for the seassick snorkelling module."""
import pytest

SEA_SICK_TABLE = [
    ["~", "No Problem"],
    ["_~~~~~~~_~__~______~~__~~_~~", "Throw Up"],
    ["______~___~_", "Throw Up"],
    ["____", "No Problem"],
    ["_~~_~____~~~~~~~__~_~", "Throw Up"],
]


@pytest.mark.parametrize("sea, result", SEA_SICK_TABLE)
def test_sea_sick(sea, result):
    """Test sea sick function that determines calmness of sea."""
    from seasick_snorkelling import sea_sick
    assert sea_sick(sea) == result
