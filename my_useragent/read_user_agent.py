import random


class UserAgent:
    def __init__(self):
        self.__list_user_agent = None
        self.__list_name_file = ['user_agent.txt','mobile_user_agent.txt']
        self.__name_file = None
        self.__i = 0
        self.__status_code = None


    def __read_file_user_agent(self):
        with open(self.__name_file,'r',encoding='utf-8') as file:
            self.__list_user_agent = file.readlines()
        #print('ok')
        #print(self.__list_user_agent)

    def get_user_agent(self,mobile=False):
        if mobile:
            self.__name_file = self.__list_name_file[1]
            self.__read_file_user_agent()
            return random.choice(self.__list_user_agent).replace('\n','')
            
        self.__name_file = self.__list_name_file[0]
        self.__read_file_user_agent()
        return random.choice(self.__list_user_agent).replace('\n','')


    def check_ua(self,status_code):
        if status_code == 200:
            self.__status_code = None
        self.__status_code = status_code
        
        
