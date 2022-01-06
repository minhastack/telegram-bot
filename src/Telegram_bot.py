import requests
class Telegram_bot: 
    
    def __init__(self, token: str, chat_id_group: str):

        self.chat_id_group = chat_id_group
        self.api_connection_url = f"https://api.telegram.org/bot{token}"
        self.message_data = requests.get(f"{self.api_connection_url}/getUpdates").json()
        self.viewed_messages = []
        self.command_list = {

            "/problema": "Olá, digite:\nstack_bot_responda e sua pergunta em seguida.\nExemplo: \n \n stack_bot_responda qual o site do minhastack?",
            "/minhastack": "Blog:\nhttp://minhastack.com/blog\n\ninstagram:\nhttps://instram.com/minhastack\n\nYoutube:\nhttps://www.youtube.com/channel/UCcHWdlaVbzVP083WlPnHiWA\n\nFacebook:\nhttps://www.facebook.com/minhastack.oficial",
            "/nodejs": "https://nodejs.org/pt-br/docs/",
            "/react": "https://pt-br.reactjs.org/tutorial/tutorial.html#setup-for-the-tutorial",
            "/python": "documentação python",
            "/mongo": "docs do mongo",
            "/express": "docs do express", 
            "/next": "docs do next", 
            "/add_commando": ['command_name', "action"] 

        }

    def message_watcher(self):

        chat_id = self.get_chat_infos()[0]
        is_correct_chat = self.chat_check(chat_id)
        message_id = self.get_message_info()["message_id"]
        message = self.get_message()
        message_is_comand = self.is_comand(message)

        if message_id in self.viewed_messages:
            print('mensage já respondida') 
        elif message_is_comand and is_correct_chat:
            self.send_message("ok")
            self.viewed_messages.append(message_id)
            print(self.viewed_messages)
        return

    
    def chat_check(self, chat_id):
        is_correct_chat = False
        if not self.chat_id_group == chat_id: 
            is_correct_chat = True
        
        return is_correct_chat

    def get_chat_infos(self)-> list:
        chat_id = self.message_data['result'][-1]['message']['chat']['id']
        group_title = self.message_data['result'][-1]['message']['chat']['title']
        return [chat_id, group_title]

    def get_message_info(self) -> dict: 
        message = self.message_data['result'][-1]
        update_id = message['update_id']
        message_id = message['message']['message_id']
        message_from = message['message']['from']['first_name']
        return {"update_id": update_id, "message_id":message_id, "message_from":message_from}

    def get_message(self) -> str:
        message = self.message_data['result'][-1]['message']['text'] 
        return message

    def send_message(self, text):
        
        chat_id = self.chat_id_group
        url = f"{self.api_connection_url}/sendMessage?chat_id={chat_id}&text={text}"
        requests.get(url)
    
    def execute_command(self, comand_message) -> str:
        response = 'teste'
        for command in self.command_list: 
            if comand_message == command:
                response = self.command_list[command]
        return response

    def is_comand(self, message) -> bool: 
        message_is_command = False
        for command in self.command_list:
            if message == command:
                message_is_command = True
        return message_is_command
