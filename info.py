import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Auto_Filters_Bot')
API_ID = int(environ.get('API_ID', '29264299'))
API_HASH = environ.get('API_HASH', '01715c2876c152106ceab149e4764ec5')
BOT_TOKEN = environ.get('BOT_TOKEN', '6686129524:AAH4UfXV5Jme04cJ5cRnhPZ1DuqkIkpPsAo')
PORT = int(environ.get('PORT', '8080'))

# Bot pics and stickers
STICKERS = (environ.get('STICKERS', 'CAACAgIAAxkBAAEGm9hjhf69CtQmXoeQ2HidYCGBFeZ4gAACxgEAAhZCawpKI9T0ydt5RysE CAACAgIAAxkBAAEGm9pjhf7I9jCDh3PpkocMNFcPJfisvwAC0wADVp29CvUyj5fVEvk9KwQ CAACAgIAAxkBAAEGm9xjhf7SH4Yc8EP5yI4e8BTH968ClwACGAADDbbSGX671giQDJU8KwQ')).split()
PICS = (environ.get('PICS', 'https://telegra.ph/file/58fef5cb458d5b29b0186.jpg https://telegra.ph/file/f0aa4f433132769f8970c.jpg https://telegra.ph/file/f515fbc2084592eca60a5.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/6045ba953af4def846238.jpg')).split()

# Bot Admins
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '5505094097').split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if id_pattern.search(index_channels) else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001532575427').split()]
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001829666061'))

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://tiniqequde:Sunny12@cluster0.vuzu197.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/Filmy_funs')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/filmy_funs_update')
USERNAME = environ.get('USERNAME', 'https://t.me/Sunnyseee')
# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "✅ I Found: <code>{query}</code>\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating} / 10</a>\n☀️ Languages: {languages}\n📀 RunTime: {runtime} Minutes\n\n🗣 Requested by: {message.from_user.mention}\n©️ Powered by: <b>{message.chat.title}</b>")
FILE_CAPTION = environ.get("FILE_CAPTION", "<i>{file_name}</i>\n\nᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ")
SHORTLINK_URL = environ.get("SHORTLINK_URL", "jnglink.in")
SHORTLINK_API = environ.get("SHORTLINK_API", "93afdd16e98ac2ba9461051503e759f4da683333")
WELCOME_TEXT = environ.get("WELCOME_TEXT", "Hello {mention}, Welcome to {title} group!")
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Filmy_funs")

# stream features vars
"""Deploy this repo: https://github.com/adarsh-goel/filestreambot"""
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "0"))
URL = environ.get("URL", "https://seeebot.onrender.com/")
                           
