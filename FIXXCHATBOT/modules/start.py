import asyncio
import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram.enums import ChatType

from FIXXCHATBOT import app
from FIXXCHATBOT.database.chats import add_served_chat
from FIXXCHATBOT.database.users import add_served_user
from FIXXCHATBOT.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


# Random start videos
ANNIE_VID = [
    "https://telegra.ph/file/fb981c15b8555e3192a5b.mp4",
    "https://telegra.ph/file/a4d90b0cb759b67d68644.mp4",
    "https://telegra.ph/file/a90ac639a094756bb3c86.mp4",
    "https://telegra.ph/file/54d944321535e898c37f5.mp4",
    "https://telegra.ph/file/b3ac2d77205d5ded860de.mp4",
    "https://telegra.ph/file/58ae4ac86ef70dc8c8f6a.mp4",
    "https://telegra.ph/file/3a74b750ca9743d351473.mp4",
    "https://telegra.ph/file/55c840c8eba0555318f0d.mp4",
    "https://telegra.ph/file/e97715885d0a0cfbddaaa.mp4",
    ""
]

# Random stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

# Random emojis
EMOJIOS = ["💀", "💔", "✅", "🧨", "⚡", "👾", "👻", "✨", "🎩", "🕊"]


# Command handler for /start and /aistart
@app.on_cmd(["start", "vashustart"])
async def start_command_handler(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        # Display loading messages
        accha = await m.reply_text(text=random.choice(EMOJIOS))
        await asyncio.sleep(1.3)
        await accha.edit("🏓FIXX..ᴍᴇᴇɴʏ..ᴍɪɴʏ..ᴍᴏᴇ✨")
        await asyncio.sleep(0.2)
        await accha.edit("__FIXX..ᴍᴇᴇɴʏ ꨄ sтαятιиg by vashu.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ꪖꪀꪀ𝓲ꫀ ꨄ︎ sтαятιиg by vashu..__")
        await asyncio.sleep(0.2)
        await accha.delete()

        # Send a random sticker
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()

        # Send a random video with a caption
        await m.reply_video(
            video=random.choice(ANNIE_VID),
            caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ {app.name}**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**\n<b>๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_video(
            video=random.choice(ANNIE_VID),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


# Command handler for /help
@app.on_cmd("help")
async def help_command_handler(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_video(
            video=random.choice(ANNIE_VID),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_video(
            video=random.choice(ANNIE_VID),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


# Command handler for /repo
@app.on_cmd("repo")
async def repo_command_handler(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )

##########################################################

WELCOME_IMG = [
    "https://telegra.ph/file/6368cf50226f851cf12b0.jpg",
    "https://telegra.ph/file/74d333a2eb853d6d340e5.png",
    "https://telegra.ph/file/e29c7352ac8a29c6d7d1c.png",
    "https://telegra.ph/file/024c4d788089a549f7c18.png",
    "https://telegra.ph/file/21a6c46b6b997c9baa507.png",
    "https://telegra.ph/file/e4205a5896e9cd1354df4.png",
    "https://telegra.ph/file/ceaee4640a3af5acdb717.png",
    "https://telegra.ph/file/98f40c919b0598586d697.png",
    "https://graph.org/file/36af423228372b8899f20.jpg",
]

WELCOME_TXT= "ᴀᴀ ɢʏᴇ ᴀᴀᴘ💗 , ᴀᴀᴘ ʜɪ ᴋᴀ ɪɴᴛᴢᴀᴀʀ ᴛʜᴀ...ᴀʙʙ ᴊᴀɴᴀ ᴍᴀᴛ ᴋᴀʜɪ ʏʜɪ ʀᴀʜᴏ ᴀᴜʀ ᴍᴇʀᴇ KO APNE GROUP MAY ADD KARLO 🤭😅"
# Welcome message for new chat members
@app.on_message(filters.new_chat_members)
async def welcome_message(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(WELCOME_IMG
