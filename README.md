# RPi Weather Monitor
Small weather monitor for Raspberry Pi, using the inky pHat as display and OpenWeather for the weather API

## Setting it up
1) Run 
~~~~
pip3 install -r requirements.txt
~~~~
1) Go to https://home.openweathermap.org/ and setup a API key, the free key should be more than fine
2) Add the key to your environment variables in ~/.bashrc with name WEATHER_API (add line 
~~~~
export WEATHER_API=[api key]
~~~~
to bashrc)

3) Set your location in the config.json file
4) Run weather.py
---
## Bonus
Run the API, this will let you control the weather monitor remotely
1) Run 
~~~~
sudo apt install nginx
~~~~
This will allow your Pi to be seen externally

2) Run 
~~~~
ip address
~~~~
And note down your external ip address

3) In the weather monitor directory run
~~~~
uvicorn api_server:app --reload --host [external ip address]
~~~~

4) In your browser go to http://[external ip]:8000/docs

