import os 
import dotenv 
import time
from src.Telegram_bot import Telegram_bot

dotenv.load_dotenv( dotenv.find_dotenv())
token = os.getenv("TELEGRAM_URL_CONNECTION")

while True:

    bot = Telegram_bot(token,'-1001592206421')
    message_info = bot.get_message_data()
    print(message_info["teste"])
    time.sleep(3)
