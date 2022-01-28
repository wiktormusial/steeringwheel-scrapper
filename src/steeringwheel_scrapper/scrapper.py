import requests
from urllib.parse import urlparse
from typing import Any
from bs4 import BeautifulSoup

stores = [
    {
        'url': 'https://www.otto.de/p/logitech-g-g923-fuer-xbox-und-pc-lenkrad-C1217986489',
    },
    {
        'url': 'https://www.coolshop.de/produkt/logitech-g923-racing-wheel-and-pedals-for-xbox-one-and-pc/2368WJ/',
    },
    {
        'url': 'https://www.kaufland.de/product/362041609/'
    },
    {
        'url': 'https://www.galaxus.de/de/s1/product/logitech-g-g923-trueforce-for-pc-and-playstation-gaming-controller-14032616'
    },
    {
        'url': 'https://www.boomstore.de/Joysticks-und-Gamepads/Logitech-G-G920-Analog-/-Digital-Lenkrad-Pedale-f%C3%BCr-PC,-Xbox-One-Schwarz.5099206058996.html'
    },
    {
        'url': 'https://www.playox.de/logitech-g923-13077149'
    },
]


class Scrapper:

    def __init__(self, url: str) -> None:
        self.url = url
        self.request = requests.get(url)
        self.storeName = self._getstorename()
        self.body = self._getrequest()

    def get_item_price(self) -> str:
        price = ''.join(self._get_price().split())
        return f'{self.storeName} - {price}'

    def _get_price(self) -> Any:
        soup = BeautifulSoup(self.body, 'html.parser')
        if self.storeName == 'www.coolshop.de':
            return soup.find("meta", property="product:price:amount")['content']
        elif self.storeName == 'www.otto.de':
            if soup.find("span", id="reducedPriceAmount"):
                return soup.find("span", id="reducedPriceAmount")['content']
            else:
                return soup.find("span", id="normalPriceAmount")['content']
        elif self.storeName == 'www.kaufland.de':
            return soup.find("div", class_="rd-buybox__price").string
        elif self.storeName == 'www.galaxus.de':
            return soup.find("meta", property="product:price:amount")['content']
        elif self.storeName == 'www.boomstore.de':
            return soup.find("div", class_="cssprice")['title']
        elif self.storeName == 'www.playox.de':
            return soup.find("meta", itemprop="price")['content']

    def _getstorename(self) -> str:
        return urlparse(self.url).netloc

    def _getstatuscode(self) -> int:
        return self.request.status_code

    def _getrequest(self) -> str:
        return self.request.text

for store in stores:
    print(Scrapper(store['url']).get_item_price())
