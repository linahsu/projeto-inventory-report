from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report
from datetime import date, datetime
from typing import List

class SimpleReport(Report):
    def __init__(self):
        self.inventories_list: List[Inventory] = []
        self.companies_product_qtd = dict()

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories_list.append(inventory)

    def generate(self) -> str:
        """Gera o relatório a partir dos produtos que estão presentes em cada um dos estoques armazenados"""
        
        oldest_manufactoring_date = date.today()
        closest_expiration_date = date.max

        for inventory in self.inventories_list:
            # faz a contagem de produtos por company no dicionário companies_product_qtd
            for product in inventory.data:
                if not product.company_name in self.companies_product_qtd:
                    self.companies_product_qtd[product.company_name] = 1
                else:
                    self.companies_product_qtd[product.company_name] += 1

                # Converts dates 'YYYY-MM-DD' into datetime objects
                date_format = "%Y-%m-%d"

                manufactoring_date = datetime.strptime(product.manufacturing_date, date_format).date()
                expiration_date = datetime.strptime(product.expiration_date, date_format).date()

                # Replace the dates in case it fits the conditionals setting the oldest manufactoring and the closest expiration dates
                if manufactoring_date < oldest_manufactoring_date:
                    oldest_manufactoring_date = manufactoring_date

                if closest_expiration_date > expiration_date > date.today():
                    closest_expiration_date = expiration_date

        largest_inventory_company = max(self.companies_product_qtd, key=self.companies_product_qtd.get)

        return (
            f"Oldest manufacturing date: {oldest_manufactoring_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory_company}"
        )
