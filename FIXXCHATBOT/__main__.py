import asyncio
import importlib
from pyrogram import idle
from FIXXCHATBOT import app
from FIXXCHATBOT.modules import ALL_MODULES


async def vashu_boot():
    try:
        await app.start()
    except Exception as ex:
print(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("FIXXCHATBOT.modules." + all_module)
print("bot Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(vashu_boot())
print("Stopping app Bot vashu...")
