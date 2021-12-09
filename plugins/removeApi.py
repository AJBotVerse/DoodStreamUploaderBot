#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.command("revoke"))
async def removeApiHandler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        userid = msg.chat.id
        if apiExist(userid):
            removeApiKey(userid)
            await msg.reply_text(
                "Your api key is removed successfully."
            )
        else:
            await msg.reply_text(
                "Your api key is not added with bot."
            )
    return

