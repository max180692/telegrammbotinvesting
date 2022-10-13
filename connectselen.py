from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from my_useragent.read_user_agent import UserAgent


#Класс для создания подключения с использованием Selenium без Gui оболочки

class GetHtmlPage:
    def __init__(self):
        self.__options = None 
        self.__ua = UserAgent()
        self.__userAgent = None

#Создание настроек для браузера Selenium

    def __setpropertise(self):
        self.__options = webdriver.ChromeOptions()
        self.__userAgent = self.__ua.get_user_agent()
        print(self.__userAgent)
        self.__options.add_argument("window-size=1280,800")
        self.__options.add_argument('--headless')
        #self.__options.add_argument('--no-sandbox')
        self.__options.add_argument('--disable-dev-shm-usage')
        self.__options.add_argument('--disable-blink-features=AutomationControlled')
        self.__options.add_argument(f'user-agent={self.__userAgent}')

#Запуск подключения и получения html кода страницы

    def get_sourcepage(self,url):
        self.__setpropertise()
        CROMEPATH = 'selen\chromedriver.exe'
        driver = webdriver.Chrome(CROMEPATH,options=self.__options)
        driver.get(url)
        source_page = driver.page_source
        driver.quit()
        return source_page