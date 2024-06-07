import time
from Abg import patch
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client
from pyrogram.enums import ParseMode
import config
import asyncio
import importlib
from pyrogram import idle
from FIXXCHATBOT.modules import ALL_MODULES
from FIXXCHATBOT.logging import LOGGER


boot = time.time()
mongo = MongoCli(config.MONGO_URL)
db = mongo.Anonymous
OWNER = config.OWNER_ID

class app(Client):
    def __init__(self):
        super().__init__(
            name="app",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="en",
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()

app = app()

async def vashu_boot():
    try:
        await app.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("FIXXCHATBOT.modules." + all_module)

    LOGGER.info(f"@{app.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(vashu_boot())
    LOGGER.info("Stopping app Bot vashu...")
