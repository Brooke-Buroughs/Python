from cgi import print_exception
from unicodedata import category, name

from .store_products import Products


class Store:
    def __init__(self,name,products):
        self.name=name
        self.products=products
class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
    def update_price(self,percent_change,is_increased):
        