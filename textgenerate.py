
class TextGenerate:

    def __init__(self,myjson):
        self.__myjson = myjson
        
    def generate_text(self):
        result_str = ""
        if isinstance(self.__myjson,list):
            for dicts in self.__myjson:
                text1 = ""
                for k in dicts:
                    text1 = k + '\n' + self.__get_str(dicts[k]).replace('\xa0','')
                result_str += text1
            return result_str
        if isinstance(self.__myjson,dict):
            for k in self.__myjson:
                result_str =  k +'\n'+'|'.join(self.__myjson[k]).replace('\xa0','')
            return result_str

    def __get_str(self,list_info):
        result_text = ""
        for i in list_info:
            if isinstance(i,list):
                result_text += '|'.join(i).replace('\xa0','') + '\n'
        return result_text

                    