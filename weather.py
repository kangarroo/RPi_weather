#!/usr/bin/env python3

from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont
import requests
import sched,time
import json
from os import environ


def update_screen(display, text_to_display, image_to_show=""):
    text = Image.new("P", display.resolution,color=display.WHITE)
    d = ImageDraw.Draw(text)
    fnt = ImageFont.truetype("./res/Mansalva-Regular.ttf",20)
    d.multiline_text((125,0), text_to_display, display.BLACK, font=fnt)
    with Image.open(get_image_path(image_to_show)) as img:
        text.paste(img,(0,0))
    display.set_image(text)
    display.show()

def get_image_path(image_to_show):
    if image_to_show == "01d":
        return("./res/weather/sun_clear.png")
    elif image_to_show == "01n":
        return("./res/weather/moon_clear.png")
    elif image_to_show == "02d":
        return("./res/weather/sun_cloud.png")
    elif image_to_show == "02n":
        return("./res/weather/moon_cloud.png")
    elif image_to_show == "03d":
        return("./res/weather/cloud.png")
    elif image_to_show == "03n":
        return("./res/weather/cloud.png")
    elif image_to_show == "04d":
        return("./res/weather/cloud_dark_cloud.png")   
    elif image_to_show == "04n":
        return("./res/weather/cloud_dark_cloud.png")  
    elif image_to_show == "09d":
        return("./res/weather/dark_cloud_rain.png")  
    elif image_to_show == "09n":
        return("./res/weather/dark_cloud_rain.png")  
    elif image_to_show == "10d":
        return("./res/weather/dark_cloud_rain.png")  
    elif image_to_show == "10n":
        return("./res/weather/dark_cloud_rain.png")  
    elif image_to_show == "11d":
        return("./res/weather/dark_cloud_lightning.png")  
    elif image_to_show == "11n":
        return("./res/weather/dark_cloud_lightning.png")  
    elif image_to_show == "13d":
        return("./res/weather/snow.png")  
    elif image_to_show == "13n":
        return("./res/weather/snow.png")
    elif image_to_show == "50d":
        return("./res/weather/mist.png")
    elif image_to_show == "50n":
        return("./res/weather/mist.png")
    else:
        return("./res/tama_nbg.png")

def get_weather(city):
    payload = {'q': city, 'units': 'metric', 'appid':environ.get('WEATHER_API')}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    return r.status_code,r.json()

def do_update(display, city):
    status, weather = get_weather(city)
    if status == 200:
        current_sit = weather["weather"][0]["main"]
        current_temp = weather["main"]["temp"]
        current_feels = weather["main"]["feels_like"]
        icon = weather["weather"][0]["icon"]
        weather_str = f"{city}\n{current_sit}\nTemp:{current_temp}°C\nFeels:{current_feels}°C"
        print(weather_str)
        update_screen(display,weather_str,icon)
    else:
        update_screen(display,"Error\ngetting\nweather!")

def update_location():
    with open("./config.json") as json_file:
        config = json.load(json_file)
    refresh_period_mins = config["refresh_period_mins"]*60
    city = config["location"]
    do_update(get_display(), city)
    return refresh_period_mins, city

def get_display():
    return auto()
    

if __name__ == "__main__":
    print("RPi Weather")
    print("K Arroo - 2022")

    display = get_display()
    
    display.set_border(display.BLACK)

    update_screen(display,"Getting ready...")
    _, city = update_location()
    s = sched.scheduler(time.time,time.sleep)
    while True:
        refresh_period_mins, city = update_location()
        s.enter(refresh_period_mins,1,do_update,kwargs={'display':display, 'city':city})
        s.run()
        
