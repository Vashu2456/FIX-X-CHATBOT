from pyrogram import filters, Client
from pyrogram.types import Message

from FIXXCHATBOT import OWNER, app
from FIXXCHATBOT.database.chats import get_served_chats
from FIXXCHATBOT.database.users import get_served_users


@app.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    ower  = len(await get_served_owner_username())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}
➻ **ᴼᵂᴺᴱᴿ :** {ᴼᵂᴺᴱᴿ_username}"""
    )
