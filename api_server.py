from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json
from weather import update_location

app = FastAPI()

class Config(BaseModel):
    location: Optional[str] = None
    refresh_period_mins: Optional[int] = None

@app.post("/config/")
def set_config(config: Config):
    with open('config.json') as config_file:
        config_json= json.load(config_file)
    test = json.loads(config.json())
    if(test["location"] != None):
        config_json["location"] = test["location"]
    if(test["refresh_period_mins"] != None):
        config_json["refresh_period_mins"] = test["refresh_period_mins"]
    with open('config.json','w') as config_file:
        json.dump(config_json, config_file, indent=2)
    update_location()
    return config  
    

@app.get("/config/")
def get_config():
    with open('config.json') as config:
        return json.load(config)


