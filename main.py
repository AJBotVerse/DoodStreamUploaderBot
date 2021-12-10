#!/usr/bin/env python3


### Importing
# Importing External Packages
from pyrogram import Client

# Importing Inbuilt Packages
import logging

# Importing Credentials & Required Data
try:
    from testexp.config import Config
except ModuleNotFoundError:
    from config import Config


### For Logs
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logging.getLogger(
    "pyrogram"
).setLevel(
    logging.WARNING
)

### Starting Bot
if __name__ == "__main__" :

    plugins = dict(
        root="plugins"
    )

    app = Client(
        "DoodStreamUploaderBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()

