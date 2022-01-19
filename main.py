import os
import dotenv 
import time
from src.Telegram_bot import Telegram_bot

dotenv.load_dotenv( dotenv.find_dotenv())
token = os.getenv("TELEGRAM_URL_CONNECTION")

bot = Telegram_bot(token,'-1001592206421')

while True:
    bot.message_watcher()
    time.sleep(2)

# teste = {
#     "update_id": 277257923,
#      "message": {
#         "message_id": 566,
#      "from": {
#         "id": 1932640952,
#      "is_bot": False,
#      "first_name": "Descolado",
#      "language_code": "en"},
#  "chat": {
#     "id": -1001592206421,
#      "title": "teste",
#      "type": "supergroup"},
#  "date": 1642594899,
# "new_chat_title": "teste"
# }
# }

# if "new_chat_title" in teste["message"]:
#     print("não é uma mensagem")
# else:
#     print("É uma mensagem")


