import os 
import dotenv 
import time
from src.Telegram_bot import Telegram_bot

dotenv.load_dotenv( dotenv.find_dotenv())
token = os.getenv("TELEGRAM_URL_CONNECTION")
bot = Telegram_bot(token,'-1001387626450')

# while True:
#     bot.message_watcher()
#     time.sleep(2)

