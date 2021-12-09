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
            apiUrl = f"https://doodapi.com/api/upload/url?key={apiKey}"
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
                        "<b>Given URL is Invalid.</b>",
                        parse_mode = "html"
                    )
            url = url.strip()
            apiUrl += f"&url={url}"
            fileID = uploadRequest(apiUrl)
            if fileID:
                fileurl = f'https://dood.la/d/{fileID}'
                await msg.reply_text(
                    f"<b>Your file will be uploaded soon😊 on this url :\n<code>{fileurl}</code></b>",
                    parse_mode = "html"
                )
            else:
                await msg.reply_text(
                    "<b>😢Unable to upload your file. Something Went Wrong.</b>",
                    parse_mode = "html"
                )
        else:
            await msg.reply_text(
                "<b>Your API Key is not Added\nAdd your API Key by using <code>/add APIKEY</code>.</b>",
                parse_mode = "html"
            ) 
    return

