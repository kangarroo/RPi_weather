import pytest
from weather import get_image_path

base_path = "./res/weather/"

@pytest.mark.parametrize("input,expected",[("01d",base_path+"sun_clear.png"),
                                           ("01n",base_path+"moon_clear.png"),
                                           ("02d",base_path+"sun_cloud.png"),
                                           ("02n",base_path+"moon_cloud.png"),
                                           ("03d",base_path+"cloud.png"),
                                           ("03n",base_path+"cloud.png"),
                                           ("04d",base_path+"cloud_dark_cloud.png"),
                                           ("04n",base_path+"cloud_dark_cloud.png"),
                                           ("09d",base_path+"dark_cloud_rain.png"),
                                           ("09n",base_path+"dark_cloud_rain.png"),
                                           ("10d",base_path+"dark_cloud_rain.png"),
                                           ("10n",base_path+"dark_cloud_rain.png"),
                                           ("11d",base_path+"dark_cloud_lightning.png"),
                                           ("11n",base_path+"dark_cloud_lightning.png"),
                                           ("13d",base_path+"snow.png"),
                                           ("13n",base_path+"snow.png"),
                                           ("50d",base_path+"mist.png"),
                                           ("50n",base_path+"mist.png"),
                                           ("BAD_INPUT","./res/tama_nbg.png")])
def test_get_image_path(input,expected):
    assert get_image_path(input) == expected
