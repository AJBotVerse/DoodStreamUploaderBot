#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.command(["start", "help"]))
async def start_handler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        if msg.text.startswith("/start"):
            reply_msg = "<b>Hi, I am Dood Stream Uploader Bot created by @AJTimePyro and his community @AJPyroVerse.\n\nWhat I can do?</b>\nI can upload video from direct/raw url to Dood Stream. Awesome isn't it?\n\n<b>How to use me?</b>\nUse /help to get info.\n\n<b>If facing any problem then ask at @AJPyroVerseGroup.</b>"
        else:
            reply_msg = "<b>📝How to use me?</b>\n1️⃣ Add your API key by using <code>/add APIKEY</code> (Generate your API Key from <a href='https://doodstream.com/settings'>here</a>).\n2️⃣Now Send any direct or raw url of any Video📽️ (If you want to add any custom name for video then Send that custom name along with url separated by <code>|</code> e.g., <code>https://example.com/file.mp4 | CustomName</code>)\n3️⃣If you want to remove your API Key from Bot, then use /revoke.\n\n<b>If facing any problem then ask at @AJPyroVerseGroup.</b>"
        await msg.reply_text(
            reply_msg,
            parse_mode = 'html'
        )
    return

