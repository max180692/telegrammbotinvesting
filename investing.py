from category import Category
from connectrequests import NewConnect
from infotable import Table
from textgenerate import TextGenerate



class Investing:

    def __init__(self):
        self.__urls = None
        self.__category = Category()
        self.__newconnect = NewConnect()
        self.__html_page = None
        self.__list_subcategory = None
        self.__data_json = self.__category.get_category()
        self.__action = False
        self.__subcategory = None
    

    def set_html_page(self,html_page=None):
        if html_page:
            self.__html_page = html_page


     
    def set_subcategory(self,data):
        if data in self.__data_json:
            self.__list_subcategory = self.__data_json[data]
            self.__action = True
        else:
            self.__action = False

    def get_action(self):
        return self.__action

    def get_subcategory(self):
        return self.__subcategory
    
    def get_list_category(self):
        return [k for k in self.__data_json.keys()]

    def get_list_subcategory(self):
        if self.__list_subcategory:
            return [ k for k in self.__list_subcategory.keys() ]

    def get_url(self):
        return self.__urls

    def set_info_subcategory(self,data):            
        if data in self.__list_subcategory:
            self.__urls = self.__list_subcategory[data]
            new_source = self.__newconnect.connect(self.__urls)
            if new_source:
                body_table = Table(new_source)
                tg = TextGenerate(body_table.info_tables())
                return tg.generate_text()
            else:
                print('error')

