

class MyJson:

    def __init__(self,title,list_info):
        self.__title = title
        self.__list_information = list_info
        
    def generate_json(self):
        text_info = []
        for tag in self.__list_information:
            if tag.find_all('td'):
                line_info = []
                for new_tag in tag.find_all('td'):
                    line_info.append(new_tag.text)
                text_info.append(line_info)
            else:
                text_info.append(tag.text)
        my_dict = {self.__title:text_info}
        return my_dict