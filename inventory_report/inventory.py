from typing import Optional, List
from inventory_report.product import Product

class Inventory:
    def __init__(self, data: Optional[List[Product]] = None) -> None:
        if not data:
            self.__data = []
        else:
            self.__data = data

    def add_data(self, data: List[Product]) -> None:
        self.__data = self.__data + data
        return self.__data

    @property
    def data(self) -> List[Product]:
        return self.__data