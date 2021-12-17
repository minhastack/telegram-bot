import requests 

class Telegram_bot: 
    
    def __init__(self, token, url):
        self.token = token 
        self.url = url
        self.message_data = requests.get(f"{self.url}/getUpdates").json()

    def get_user_info(self) -> list:
        data_message = self.message_data
        chat_id = data_message['result'][-1]['message']['from']['id']
        first_name = data_message['result'][-1]['message']['from']['first_name']
        user_info = [chat_id, first_name]
        return user_info
    
    def response_user_message(self, chat_id, text) -> None:
        url = f"{self.url}/sendMessage?chat_id={chat_id}&text={text}"
        requests.get(url)
        return


    def get_message(self) -> str :
        data_message = self.message_data
        text_message = data_message['result'][-1]['message']['text']
        return text_message

    def save_email(self) -> str: 
        data_message = self.message_data
        text_message = data_message['result'][-1]['message']['text']
        is_email = self.is_email(text_message)
        user_info = self.get_user_info()
        if(is_email):
            self.response_user_message(user_info[0], f"{user_info[1]}, não se preocupe. Seus dados estão a salvo ;)")   

        else:
            self.response_user_message(user_info[0], f"{user_info[1]}, eu e você sabemos que isso não é um email")   
    
    @classmethod
    def is_email(cls, message: str)-> None:
        if "@gmail.com" in message: 
            return True
        else: 
            return False
     
