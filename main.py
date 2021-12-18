import os 
import dotenv 
from src.Telegram_bot import Telegram_bot


def run():

    dotenv.load_dotenv( dotenv.find_dotenv())
    token = os.getenv("TELEGRAM_URL_CONNECTION")
    url_base = f"https://api.telegram.org/bot{token}"

    bot1 = Telegram_bot(token, url_base)
    user_info = bot1.get_user_info()
    user_message = bot1.get_message()
    get_email = bot1.save_email()
    print(user_info, " Mensagem: " ,user_message)

run()
