import os

class Config:
    API_ID = int(os.getenv("API_ID", "0"))         # set on Railway / .env
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/slmusicmania")
    DEV_CONTACT = os.getenv("DEV_CONTACT", "https://t.me/deweni2")
