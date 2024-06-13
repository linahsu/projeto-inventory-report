from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        """Lê um arquivo JSON, instancia objetos de Product e retorna uma lista de Product"""
        
        with open(self.path) as file:
            products_info = json.load(file)

        products_list = list()

        for product_info in products_info:
            product = Product(
                product_info["id"],
                product_info["product_name"],
                product_info["company_name"],
                product_info["manufacturing_date"],
                product_info["expiration_date"],
                product_info["serial_number"],
                product_info["storage_instructions"],
            )
            products_list.append(product)
        
        return products_list


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
