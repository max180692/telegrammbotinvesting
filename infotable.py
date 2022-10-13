import lxml
from bs4 import BeautifulSoup as bs
from myjson import MyJson

# Класс по парсингу таблиц из сайта

class Table:
    def __init__(self,source):
        self.__soup = bs(source,'lxml')
        self.__soup_body = None
        self.__list_table = None
        self.__inform = False
        self.__not_table = None
        self.__table = list()
        self.__info_no_table = None

#Проверка наличии таблицы

    def __check_body_table(self):
        self.__list_table = self.__soup_body.select('table.genTbl')
        self.__not_table = self.__soup_body.find('div',{'class':'fullHeaderTwoColumnPage--top'})
        if self.__not_table:
            self.__inform = True
        else:
            self.__inform = False
            
        
# Поиск елементов в разных блоках

    def __find_table(self):
        if self.__soup.main:
            self.__soup_body = self.__soup.main
            self.__check_body_table()
        elif self.__soup.section:
            self.__soup_body = self.__soup.section
            self.__check_body_table()
            
#Функция поиска если не таблица

    def __find_not_table(self):
        list_title = self.__soup_body.find('h1')
        information = self.__not_table.select_one('div.top.bold.inlineblock').select('span')
        myjson = MyJson(list_title.text,information)
        self.__info_no_table = myjson.generate_json()


#Функция вывода если таблица

    def __output_info_table(self,list_title):
        if len(list_title) == len(self.__list_table):
            for i in range(len(list_title)):
                title = list_title[i].text
                list_tag_td = self.__list_table[i].find_all('tr')
                myjson = MyJson(title, list_tag_td)
                self.__table.append(myjson.generate_json())

#Вывод информации с сайта

    def info_tables(self):
        self.__find_table()
        if self.__inform:
            self.__find_not_table()
            return self.__info_no_table
        else:
            if len(self.__list_table)>1:
                list_title_h2 = self.__soup_body.find_all('h2')
                list_title_h3 = self.__soup_body.find_all('h3')
                if list_title_h2:
                    self.__output_info_table(list_title_h2)
                    return self.__table
                elif list_title_h3:
                    self.__output_info_table(list_title_h3)
                    return self.__table
            elif len(self.__list_table) == 1:
                list_title = self.__soup_body.find_all('h1')
                self.__output_info_table(list_title)
                return self.__table



