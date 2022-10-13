import lxml
from bs4 import BeautifulSoup as bs
import json
import os
from settingsparser import URL


#Класс Category  служит для получения категорий с сайта

class Category:
    def __init__(self):
        self.__dict_urls = None
        self.__check = False
        self.__data = None
        #self.lxml = lxml

# Проверка наличия файла если фаил есть, то выставляем параметр self.__check = True

    def __check_file(self):
        if os.path.isfile('data.json'):
            self.__check = True
# Запуск проверки наличия файла если он есть, то возврящаем значение True или False если его нет
    def get_check(self):
        self.__check_file()
        return self.__check


# Обработка данных из файла

    def get_category(self,source=None):
        self.__check_file()
        if self.__check:
            self.read_json()
            return self.__data
        soup = bs(source,'lxml')
        list_li = [li.a.text.lower().strip() for li in soup.select_one('ul.subMenuNav').select('li.row')]
        list_ul_main = [ul.select('a') for ul in soup.select_one('ul.subMenuNav').select('ul.main')]
        self.__dict_urls = dict()
        if len(list_li) == len(list_ul_main):
            for i in range(len(list_li)):
                self.__dict_urls[list_li[i]] = {ur.text.lower():URL+ur['href'] for ur in list_ul_main[i]}
        print(self.__dict_urls)
        self.create_json()
        return self.__dict_urls

#Создание файла и запись данных в него

    def create_json(self):
        with open('data.json','w') as file:
            json.dump(self.__dict_urls,file)

# Чтение файла

    def read_json(self):
        with open('data.json') as file:
            self.__data = json.load(file)
        