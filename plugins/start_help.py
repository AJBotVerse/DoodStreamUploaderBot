#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.command(["start", "help"]))
async def start_handler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        if msg.text.startswith("/start"):
            reply_msg = "Hi"
        else:
            reply_msg = "Hello"
        await msg.reply_text(
            reply_msg,
            parse_mode = 'html'
        )
    return

