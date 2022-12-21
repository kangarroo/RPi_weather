import pytest
from unittest.mock import patch, mock_open, MagicMock
#from weather import get_image_path, update_location,do_update,get_display
import weather
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
    assert weather.get_image_path(input) == expected

json_text = '''
{
    "location":"London,uk",
    "refresh_period_mins":10
}
'''
@patch("weather.do_update")
@patch("weather.get_display", return_value={})
def test_update_location(mock_do_update, mock_get_display):
    # do_update = MagicMock()
    # get_display = MagicMock(return_value={})
    with patch("builtins.open",mock_open(read_data=json_text)) as mock_file:
        refresh_mins,city = weather.update_location()
        assert refresh_mins == 600
        assert city == "London,uk"
        mock_do_update.assert_called_with({},"London,uk")
        

