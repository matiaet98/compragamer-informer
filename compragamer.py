import requests
from bs4 import BeautifulSoup


class compragamer:
    def __init__(self):
        self.url = 'https://compragamer.com/index.php'
        self.params = {
            'seccion': '3'
        }

    def search(self, criteria):
        self.params['criterio'] = criteria
        req = requests.get(url=self.url, params=self.params)
        soup = BeautifulSoup(req.text, 'html.parser')
        items = soup.findAll('li', attrs={'class': 'products__item'})
        articulos = []
        for item in items:
            producto = item \
                .findChild('div', attrs={'class': 'products__wrap clearfix'})
            tipo_boton = producto \
                .findChild('footer', attrs={'class': 'products-btns'}) \
                .findChild()
            if (tipo_boton.name == 'div'):
                continue  # Si no hay stock, sigo con el proximo producto
            descripcion = producto \
                .findChild('h4', attrs={'class': 'products__name'}) \
                .findChild('a') \
                .contents[0].strip()
            valor = producto \
                .findChild('div', attrs={'class': 'products__inner'}) \
                .findChild('span', attrs={'class': 'products__price-new'}) \
                .findChild('font') \
                .contents[0].strip()
            articulos.append(descripcion + ": " + valor)
        return articulos
