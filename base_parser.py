import json
import requests
from bs4 import BeautifulSoup

class BaseParser:
    def __init__(self, category):
        self.category = category
        self.URL = 'https://upg.uz/ru/categories/'

    def get_soup(self):
        res = requests.get(self.URL + self.category)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup
        else:
            return 'Xato katigoriya'


    @staticmethod
    def save_json(data, filename):
        with open(f'{filename}.json', mode='w', encoding='utf-8')as file:
            json.dump(data,file, ensure_ascii=False,indent=4)






