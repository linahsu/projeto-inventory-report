from inventory_report.reports.simple_report import SimpleReport

class CompleteReport(SimpleReport):
    def generate(self) -> str:
        """Uses the implementation from SimpleReport and adds information of inventory per company"""
        
        first_part = super().generate()

        second_part = ""
        for company, quantity in self.companies_product_qtd.items():
            second_part += f"- {company}: {quantity}\n"

        return first_part + "\nStocked products by company:\n" + second_part
