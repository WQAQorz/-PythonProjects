import requests
from bs4 import BeautifulSoup
from common_tools.os_operator import OsOperator


class WebSpider:
    def __init__(self, url=""):
        self.url = url
        self.source_text = ""
        self.my_session = requests.Session()

    def login(self):
        login_url = """https://i.mi.com/sts?sign=mF32YtfY7XReThOa0pZzXhZXJ0U%3D&followup=https%3A%2F%2Fi.mi.com%2F
        &sid=i.mi.com&d=wb_ae2af0da-9de2-463a-91d9-cacb2cbdea01&ticket=0&pwd=1&p_ts=1697813029000&fid=0&p_lm=1&auth
        =kbFivvigD5FqHy3E85ouUkN9Ur9H0x1AJcRmQ7evmnDcZl2qxuEjXVTHcf5BmMMXdpTRZLn3pkxW5pDH%2FIWYhGO%2BC
        %2B3jbgf0Novwsrk0o5uQ51L14%2FXzvf%2B3xSdR8gCfsvzxDT2UF4vVEVAfDGYUqGAiczP8wYirB7GeFS1CYXw%3D&m=513&_group
        =DEFAULT&tsl=1&p_ca=0&p_ur=CN&p_idc=China&nonce=DPrqeugI5Q0Br8az&_ssign=HfUSdYuwmkWryfhveKqL%2Fppf430%3D"""

        header_str = """User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36;;;;;"""

        self.my_session.headers = self.str_to_dict(header_str, delimiter=";;;;;")
        self.my_session.get(url=login_url)

    def get_source(self):
        response = self.my_session.get(self.url)
        self.source_text = response.text

    def get_specific_page(self, url):
        response = self.my_session.get(url)
        res = response.text
        return res

    def parse(self):
        soup = BeautifulSoup(self.source_text, 'html.parser')
        pass

    def save_txt(self):
        pass

    def save_word(self):
        pass

    @staticmethod
    def str_to_dict(header_str: str, delimiter=";"):
        headers = header_str.split(delimiter)
        res = {}
        for header in headers:
            temp = header.split("=")
            if len(temp) < 2:
                continue
            res[temp[0]] = temp[1]

        return res


if __name__ == "__main__":
    spider = WebSpider(url="https://i.mi.com/#/")
    spider.login()
    spider.get_specific_page("https://i.mi.com/note/full/page/?ts=1697861728791&limit=200")
    spider.get_source()
    spider.parse()
    pass
