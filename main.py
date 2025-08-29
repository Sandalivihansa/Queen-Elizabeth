import logging
import asyncio
from pyrogram import Client
from config import Config

# import modules (explicit import so we can register)
from modules import adult

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Client name can be anything; using env credentials from config
app = Client(
    "telegram-bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    # no plugins dict used, we import & register explicitly
)

def main():
    # register modules that need explicit register()
    adult.register(app)

    logger.info("Starting bot...")
    app.run()  # blocks and runs until stopped
    logger.info("Bot stopped.")

if __name__ == "__main__":
    main()
