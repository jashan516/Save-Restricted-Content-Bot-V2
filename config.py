# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24955192"))
API_HASH = getenv("API_HASH", "11b37ff7dce98fee45c1445249674105")
BOT_TOKEN = getenv("BOT_TOKEN", "7804285182:AAH4CwnPPy_LN2huo12rwTM9ujwQ1RTeWqU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "https://t.me/Jass_beniwal").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rs92573993688:pVf4EeDuRi2o92ex@cluster0.9u29q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "https://t.me/+_9Nv7xtx-6M0ZTY1")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002377143302"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "telegram.org")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
