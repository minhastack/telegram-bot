import requests
class Telegram_bot: 
    
    def __init__(self, token: str, chat_id_group: str):

        self.chat_id_group = chat_id_group
        self.api_connection_url = f"https://api.telegram.org/bot{token}"
        self.last_message = requests.get(f"{self.api_connection_url}/getUpdates").json()['result'][-1]
        self.answered_messages = []
        self.command_list = {

            "/problema": "Olá, digite:\nstack_bot_responda e sua pergunta em seguida.\nExemplo: \n \n stack_bot_responda qual o site do minhastack?",
            "/minhastack": "Blog:\nhttp://minhastack.com/blog\n\ninstagram:\nhttps://instram.com/minhastack\n\nYoutube:\nhttps://www.youtube.com/channel/UCcHWdlaVbzVP083WlPnHiWA\n\nFacebook:\nhttps://www.facebook.com/minhastack.oficial",
            "/nodejs": "https://nodejs.org/pt-br/docs/",
            "/react": "https://pt-br.reactjs.org/tutorial/tutorial.html#setup-for-the-tutorial",
            "/python": "documentação python",
            "/mongo": "docs do mongo",
            "/express": "docs do express", 
            "/next": "docs do next", 
        }
    

    def get_message_data(self) -> dict: 
        message = self.last_message
        update_id = message['update_id']
        message_id = message['message']['message_id']
        message_from = message['message']['from']['first_name']
        text  = message['message']['text']
        

        return {
            "message_text": text, 
            "update_id": update_id, 
            "message_id":message_id, 
            "message_from":message_from,
            }
        
    def chat_check(self, chat_id) -> bool:
        is_correct_chat = False
        if not self.chat_id_group == chat_id: 
            is_correct_chat = True
        return is_correct_chat

    def get_chat_infos(self)-> dict:
        chat_infos = {}        

        chat_type = self.last_message['message']['chat']["type"]
        chat_title = self.last_message['message']['chat']["title"]
        chat_id = self.last_message['message']['chat']['id']

        is_correct_chat = self.chat_check(chat_id)
        
        if is_correct_chat:
            chat_infos["chat_id"] = chat_id 
            chat_infos["chat_type"] = chat_type 
            chat_infos["chat_title"] = chat_title

        return chat_infos

    def send_message(self, text):
        chat_id = self.chat_id_group
        url = f"{self.api_connection_url}/sendMessage?chat_id={chat_id}&text={text}"
        requests.get(url)
    
    def execute_command(self, comand_message) -> str:
        response = ''
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
