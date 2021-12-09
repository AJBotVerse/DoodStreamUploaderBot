#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("BOT_TOKEN", "") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("API_ID", "0")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", None)) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "") # Get from MongoDB Atlas

