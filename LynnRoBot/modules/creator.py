import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jebot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>
<b>♞ Developer:</b> <a href="https://t.me/Didiktea">Didiktea 🇱🇰</a>
<b>♞ Support:</b> <a href="https://t.me/puituflynn">Mizo Android Users</a>
<b>♞ Youtube:</b> <a href="https://m.youtube.com/channel/UCRVFdrBy_I-_hNL3vgONbuQ">Youtube Channel</a>
<b>~ @Didiktea</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

print(
    """
Bot Started!
Join @puituflynn
"""
)

Jebot.run()
