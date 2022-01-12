import requests
class Telegram_bot: 
   
    def __init__(self, token: str, chat_id_group: str):

        self.chat_id_group = chat_id_group
        self.api_connection_url = f"https://api.telegram.org/bot{token}"
        self.answered_messages = []
        self.command_list = {

            "/comando":"Comandos disponíveis:\n\n/minhastack - Retorna nossas redes sociais.\n\n/node - retorna a documentação do NodeJS\n\n/react - retorna a documentação do react\n\n/python - retornar a documentação do python\n\n/mongo - retorna a documentação do mongo\n\n/express - retorna a documentação do express\n\n/next - retorna a documentação do nextJS",
            "/minhastack": "Blog:\nhttp://minhastack.com/blog\n\ninstagram:\nhttps://instram.com/minhastack\n\nYoutube:\nhttps://www.youtube.com/channel/UCcHWdlaVbzVP083WlPnHiWA\n\nFacebook:\nhttps://www.facebook.com/minhastack.oficial",
            "/node": "https://nodejs.org/pt-br/docs/",
            "/react": "https://pt-br.reactjs.org/tutorial/tutorial.html#setup-for-the-tutorial",
            "/python": "https://docs.python.org/pt-br/3/",
            "/mongo": "https://docs.mongodb.com/",
            "/express": "https://expressjs.com/", 
            "/next": "https://nextjs.org/docs/getting-started", 
        }

    def message_watcher(self):
        
        message_data = self.get_message_data()

        chat_id = self.get_chat_infos(message_data)["chat_id"]
        print(f"###{chat_id}###")
        is_correct_chat = self.chat_check(chat_id)
        message = message_data["message_text"]

        message_is_command = self.is_comand(message)
        update_id = message_data["update_id"]
        
        all_right = message_is_command and is_correct_chat and not (update_id in self.answered_messages)

        if all_right:
                response = self.execute_command(message)
                self.send_message(response)
                self.answered_messages.append(update_id)
                self.cleanup_ansewered_messages()

    def get_message_data(self) -> dict: 
        message  = requests.get(f"{self.api_connection_url}/getUpdates").json()
        message_data = {}
        
        if len(message) > 0: # significa que tem mensagem disponível e não gera error de list index of range 
            message_data["data"] = message
            message_data["update_id"] = message["result"][-1]["update_id"]
            message_data["message_id"] = message["result"][-1]["message"]["message_id"]
            message_data["message_from"] = message["result"][-1]["message"]["from"]["first_name"]
            message_data["message_text"]  = message["result"][-1]["message"]["text"]
        return message_data

    def chat_check(self, chat_id) -> bool:
        is_correct_chat = False
        if not self.chat_id_group == chat_id: 
            is_correct_chat = True
        return is_correct_chat

    def get_chat_infos(self, message_data)-> dict:
        chat_infos = {}        

        chat_type = message_data["data"]["result"][-1]["message"]["chat"]["type"]
        chat_title = message_data["data"]["result"][-1]["message"]["chat"]["title"]
        chat_id = message_data["data"]["result"][-1]["message"]["chat"]["id"]

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

    def message_is_eddited(self, message: dict):
        pass

    def cleanup_ansewered_messages(self) -> None:
        if len(self.answered_messages) > 2: 
            self.answered_messages.pop()

    def execute_command(self, comand_message) -> str:
        response = ""
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
