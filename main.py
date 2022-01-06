import os 
import dotenv 
import time
from src.Telegram_bot import Telegram_bot

dotenv.load_dotenv( dotenv.find_dotenv())
token = os.getenv("TELEGRAM_URL_CONNECTION")

while True:

    bot = Telegram_bot(token,'-1001592206421')
    bot.message_watcher()
    
    time.sleep(3)

# ['Descolado', 1932640952] - chat_id de derminado usuário
# 'chat': {'id': -1001592206421, ] - chat id de um determinado grupo
 