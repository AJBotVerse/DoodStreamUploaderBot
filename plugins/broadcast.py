#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Global Variable
fileName = 'broadcast'


### Broadcast Handler
@Client.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler(bot:Update, msg:Message):
    try:
        #Extracting Broadcasting Message
        message = msg.text.split('/broadcast ')[1]
    except IndexError:
        await msg.reply_text(
            "<b>Broadcast can't be empty.😒</b>",
            parse_mode = 'html'
        )
    except Exception as e:
        await bot.send_message(Config.OWNER_ID, line_number(fileName, e))
    else:
        #Getting User`s Id from Database
        for userid in [document['userid'] for document in collection_api_key.find()]:
            try:
                #Sending Message One By One
                await bot.send_message(userid, message)
            except exceptions.bad_request_400.UserIsBlocked:
                #User Blocked the bot
                pass
            except Exception as e:
                await bot.send_message(Config.OWNER_ID, line_number(fileName, e))
    return

