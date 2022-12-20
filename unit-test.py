import pytest
from weather import get_image_path

@pytest.mark.parametrize("input,expected",[("01d","./res/weather/sun_clr.png")])
def test_get_image_path(input,expected):
    assert get_image_path(input) == expected
