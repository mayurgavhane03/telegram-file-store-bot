import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25517360"))
  API_HASH = os.environ.get("API_HASH", "011e52db3b8390422cb2510d04d74fc9")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7498595019:AAE1lh3HL-B7Pgkl_WA9io-2S4661vJ9KdM")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Your_File_Is_Here_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "1002178820767"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "eaed8919e95e5867ef14f92cb156ce7a4615ec0b")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6524542196"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://JobTask:JobTask@cluster0.sivitpp.mongodb.net/")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "1002169310895")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1002244247095"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 

"""
  ABOUT_DEV_TEXT = f"""..
"""
  HOME_TEXT = """..
"""
