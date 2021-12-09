#!/usr/bin/env python3


### Importing
# Importing External Packages
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import exceptions, UserNotParticipant
from pymongo import MongoClient

# Importing Inbuilt Packages
import __main__
import asyncio
from inspect import currentframe

# Importing Credentials & Required Data
try:
    from testexp.config import Config
except ModuleNotFoundError:
    from config import Config
finally:
    mongoSTR = Config.MONGO_STR


### Connecting To Database
if mongoSTR:
    mongo_client = MongoClient(mongoSTR)
    db_user = mongo_client['DoodStream_Uploader']
    collection_user = db_user['members']


### Defining Some Functions
#Function to find error in which file and in which line
def line_number(fileName, e):
    cf = currentframe()
    return f'In {fileName}.py at line {cf.f_back.f_lineno} {e}'

#Checking User whether he joined channel and group or not joined.
async def search_user_in_community(bot, update):
    try:
        await bot.get_chat_member('@AJPyroVerse', update.chat.id)
        await bot.get_chat_member('@AJPyroVerseGroup', update.chat.id)
    except UserNotParticipant:
        await update.reply_text("", parse_mode = 'html',reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton('Join our Channel.',url = 'https://t.me/AJPyroVerse')],
        [InlineKeyboardButton('Join our Group.',url = 'https://t.me/AJPyroVerseGroup')]
        ]))
        return
    except exceptions.bad_request_400.ChatAdminRequired:
        return True
    except Exception as e:
        await bot.send_message(Config.OWNER_ID, line_number("", e))
        return True
    else:
        return True

