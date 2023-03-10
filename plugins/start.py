"""
Apache License 2.0
Copyright (c) 2022 @LazyDeveloper
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/LazyDeveloper 
Repo Link : https://github.com/LazyDeveloperrT
License Link : https://github.com/LazyDeveloperr/Lazy-Renamer-u-Pro-max/blob/main/LICENSE
"""

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"š Hello {user.mention} \nšø'š š° šššššš šµššš šššššš+šµššš šš ššššš š²ššššššš š±š¾š šššš šæšššššššš ššššššššš & š²ššššš š²šššššš ššššššš!"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton("š¼ š³š“šš š¼", callback_data='dev')
        ],[
        InlineKeyboardButton('š¢ ššæš³š°šš“š', url='https://t.me/z_harbour'),
        InlineKeyboardButton('šæ24Ć7 Moviesšæ', url='https://t.me/blackest_harbour')
        ],[
        InlineKeyboardButton('š š°š±š¾šš', callback_data='about'),
        InlineKeyboardButton('ā¹ļø š·š“š»šæ', callback_data='help')
        ]])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
    

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__Click START-RENAME and then send a file name to me.....__**\n**File Name** :-`{filename}`\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("š ššš°šš šš“š½š°š¼š“ š", callback_data="rename") ],
                   [ InlineKeyboardButton("āļø š²š°š½š²š“š» āļø", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__Click START-RENAME and then send a file name to me.....__**\n**File Name** :- `{filename}`\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("š ššš°šš šš“š½š°š¼š“ š", callback_data="rename") ],
                   [ InlineKeyboardButton("āļø š²š°š½š²š“š» āļø", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""š Hello {query.from_user.mention} \nšø'š š° šššššš šµššš šššššš+šµššš šš ššššš š²ššššššš š±š¾š šššš šæšššššššš ššššššššš & š²ššššš š²šššššš ššššššš! """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("š¼ š³š“šš š¼", callback_data='dev')                
                ],[
                InlineKeyboardButton('š¢ ššæš³š°šš“š', url='https://t.me/mdisk_bots'),
                InlineKeyboardButton('šæ24Ć7 Seriesšæ', url='https://t.me/z_harbour_files')
                ],[
                InlineKeyboardButton('š š°š±š¾šš', callback_data='about'),
                InlineKeyboardButton('ā¹ļø š·š“š»šæ', callback_data='help')
                ]]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #ā ļø don't change source code & source link ā ļø #
               InlineKeyboardButton("Mdisk_BOT", url="https://t.me/Mdisk_Link_Downloader_Bot")
               ],[
               InlineKeyboardButton("ā¤ļøāš„Telegraph Botā¤ļøāš„", url='MdiskLinksSearchBot')
               ],[
               InlineKeyboardButton("š š²š»š¾šš“", callback_data = "close"),
               InlineKeyboardButton("āļø š±š°š²šŗ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #ā ļø don't change source code & source link ā ļø #
               InlineKeyboardButton("ā£ļøUpdates", url="")
               ],[
               InlineKeyboardButton("šæMoviesšæ", url="https://t.me/z_harbour")
               ],[
               InlineKeyboardButton("š š²š»š¾šš“", callback_data = "close"),
               InlineKeyboardButton("āļø š±š°š²šŗ", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #ā ļø don't change source code & source link ā ļø #
               InlineKeyboardButton("šSearch", url="https://t.me/z_harbour_files")
               ],[
               InlineKeyboardButton("šSearch š·š¾š šš¾ š¼š°šŗš“", url="https://t.me/z_harbour")
               ],[
               InlineKeyboardButton("š š²š»š¾šš“", callback_data = "close"),
               InlineKeyboardButton("āļø š±š°š²šŗ", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





