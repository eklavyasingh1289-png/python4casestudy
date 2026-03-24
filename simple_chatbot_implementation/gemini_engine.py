import google.generativeai as clanker
import os

class GeminiClient:
    def __init__(self,api_key, model_name="gemini-3-flash-preview"):
        clanker.configure(api_key=api_key)
        self.model = clanker.GenerativeModel(model_name)
        self.chat_session = self.model.start_chat(history=[])


    def send_msg(self,user_input):
        try:
            response = self.chat_session.send_message(user_input)
            return response.text

        except Exception as e:
            return f"{e}"
