#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.command("add"))
async def addApiHandler(bot:Update, msg:Message):
    splitMessage = msg.text.split(' ')
    if len(splitMessage) == 2:
        userid = msg.chat.id
        if not apiExist(userid):
            apiKey = splitMessage[1]
            if await isApiValid(apiKey, bot, msg):
                addApiKey(apiKey, userid)
                await msg.reply_text(
                    "Api added successful."
                )
        else:
            await msg.reply_text(
                "Your Api already added."
            )
    else:
        await msg.reply_text(
            "Invalid Command"
        )

