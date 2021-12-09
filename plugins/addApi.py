#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.command("add"))
async def addApiHandler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        splitMessage = msg.text.split(' ')
        if len(splitMessage) == 2:
            userid = msg.chat.id
            if not apiExist(userid):
                apiKey = splitMessage[1]
                if await isApiValid(apiKey, bot, msg):
                    addApiKey(apiKey, userid)
                    await msg.reply_text(
                        "<b>Your API Key has been added successfully🥳🥳.</b>",
                        parse_mode = "html"
                    )
            else:
                await msg.reply_text(
                    "<b>Your API Key is already added🤪.</b>",
                    parse_mode = "html"
                )
        else:
            await msg.reply_text(
                "<b>Invalid Command⛔\nSend API Key like this <code>/add APIKEY</code>\n\nIf facing any problem🥲 then ask at😊 @AJPyroVerseGroup</b>",
                parse_mode = "html"
            )
    return

