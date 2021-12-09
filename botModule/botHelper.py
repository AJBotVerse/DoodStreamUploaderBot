#!/usr/bin/env python3


### Importing
# Importing External Packages
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import exceptions, UserNotParticipant
from pyrogram.types import Update, Message
from pymongo import MongoClient
from requests import get

# Importing Inbuilt Packages
import __main__
from inspect import currentframe

# Importing Credentials & Required Data
try:
    from testexp.config import Config
except ModuleNotFoundError:
    from config import Config
finally:
    mongoSTR = Config.MONGO_STR


### Connecting To Database
mongo_client = MongoClient(mongoSTR)
db_user = mongo_client['DoodStream_Uploader']
collection_api_key = db_user['apiKey']


### Global Varaiable
fileName = "botHelper"


### Defining Some Functions
#Function to find error in which file and in which line
def line_number(fileName, e):
    cf = currentframe()
    return f'In {fileName}.py at line {cf.f_back.f_lineno} {e}'

#Checking User whether he joined channel and group or not joined.
async def search_user_in_community(
    bot : Update,
    update : Message
    ):
    try:
        await bot.get_chat_member(
            '@AJPyroVerse',
            update.chat.id
        )
        await bot.get_chat_member(
            '@AJPyroVerseGroup',
            update.chat.id
        )
    except UserNotParticipant:
        await update.reply_text(
            "<b>Seems like you haven't joined our community😢.</b>",
            parse_mode = 'html',
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            'Join our Channel.',
                            url = 'https://t.me/AJPyroVerse'
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            'Join our Group.',
                            url = 'https://t.me/AJPyroVerseGroup'
                        )
                    ]
                ]
            )
        )
        return
    except exceptions.bad_request_400.ChatAdminRequired:
        return True
    except Exception as e:
        await bot.send_message(
            Config.OWNER_ID,
            line_number(
                fileName,
                e
            )
        )
        return True
    else:
        return True

def apiExist(
    userid : int
    ):
    result = collection_api_key.find_one(
        {
            'userid' : userid
        }
    )
    if result:
        return result
    return

async def isApiValid(
    apiKey : str,
    bot : Update,
    msg : Message
    ):
    try:
        res = get(
            f"https://doodapi.com/api/account/info?key={apiKey}"
        )
    except Exception as e:
        await bot.send_message(
            Config.OWNER_ID,
            line_number(
                fileName,
                e
            )
        )
        await msg.reply_text(
            "<b>While Checking API Key something went wrong.</b>",
            parse_mode = "html"
        )
    else:
        if res.status_code == 200:
            responseData = res.json()
            if responseData['msg'] == 'OK':
                return True
            else:
                await msg.reply_text(
                    "<b>Given API Key is Invalid😒.</b>",
                    parse_mode = "html"
                )
        else:
            await msg.reply_text(
                "<b>While Checking API Key something went wrong.</b>",
                parse_mode = "html"
            )
    return

def addApiKey(apiKey, userid):
    collection_api_key.insert_one(
        {
            'userid' : userid,
            'apiKey' : apiKey
        }
    )

def removeApiKey(userid):
    collection_api_key.delete_one(
        {
            'userid' : userid
        }
    )

def uploadRequest(url):
    res = get(url)
    if res.status_code == 200:
        responseData = res.json()
        if responseData['msg'] == 'OK':
            fileID = responseData['result']['filecode']
            return fileID
    return

