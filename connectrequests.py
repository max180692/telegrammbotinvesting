import requests
from my_useragent.read_user_agent import UserAgent

#Класс подключения без использования Selenium

class NewConnect:
    def __init__ (self):
        self.ua = UserAgent()
        self.session = requests.Session()

#Подключение с использованием рандомных UserAgent

    def connect(self,url,mobile=False):
        headers = {'user-agent':self.ua.get_user_agent(mobile=mobile)}
        response = self.session.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
