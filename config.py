import os

class Config:
    API_ID = int(os.getenv("API_ID", "5047271"))         # set on Railway / .env
    API_HASH = os.getenv("API_HASH", "047d9ed308172e637d4265e1d9ef0c27")
    BOTOKEN = os.getenv("BO_TOKEN", "7896090354:AAEXKm3tq0hGfWicVAdphaS_1Amu5YxAawY")
    OWNER_ID = int(os.getenv("OWNER_ID", "1451534504"))
    SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/slmusicmania")
    DEV_CONTACT = os.getenv("DEV_CONTACT", "https://t.me/deweni2")
