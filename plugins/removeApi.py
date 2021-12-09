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
                "<b>Your API Key is removed successfully😢.\nYou can add again by using <code>/add APIKEY</code>.</b>",
                parse_mode = "html"
            )
        else:
            await msg.reply_text(
                "<b>I am unable😓 to find your API Key in database.\nMake sure it was added before😒.</b>",
                parse_mode = "html"
            )
    return

