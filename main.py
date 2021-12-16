import requests
import dotenv
import os
import time

dotenv.load_dotenv( dotenv.find_dotenv())

token = os.getenv("TELEGRAM_URL_CONNECTION")

url_base = f"https://api.telegram.org/bot{token}"

run = True
count = 0

while run:
    res = requests.get(url_base + "/getUpdates").json()
    messages_number = len(res['result'])

    print(res['result'][count]['message']['text'])

    count += 1

    if(count == messages_number): 
        run = False
    time.sleep(1) 


