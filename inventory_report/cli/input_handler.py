from typing import List
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    if report_type == "simple":
        simple_report = SimpleReport()
    elif report_type == "complete":
        complete_report = CompleteReport()
    else:
        raise ValueError("Report type is invalid.")
    
    for file in file_paths:
        if file.endswith(".json"):
            products_list = JsonImporter(file).import_data()
            inventory = Inventory(products_list)
        elif file.endswith(".csv"):
            products_list = CsvImporter(file).import_data()
            inventory = Inventory(products_list)
        else:
            continue
        
        if report_type == "simple":
            simple_report.add_inventory(inventory)
        else:
            complete_report.add_inventory(inventory)

    return simple_report.generate() if report_type == "simple" else complete_report.generate()
