#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.regex(r'^http(.*)'))
async def urlUploaderHandler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        userid = msg.chat.id
        result = apiExist(userid)
        if result:
            apiKey = result['apiKey']
            apiUrl = f"https://doodapi.com/api/upload/url?key={apiKey}" #&url={upload_url}
            message = msg.text
            if '|' in message:
                url, filename = message.split("|")
                filename = filename.strip()
                if " " in filename:
                    filename = '_'.join(filename.split(' '))
                apiUrl += f"&new_title={filename}"
            else:
                url = msg.text
                if " " in url:
                    return await msg.reply_text(
                        "Invalid Url"
                    )
            url = url.strip()
            apiUrl += f"&url={url}"
            uploadRequest(url)
        else:
            await msg.reply_text(
                "Your Api is not Added."
            )
        
    return