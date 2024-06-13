import pytest
from inventory_report.product import Product

@pytest.fixture
def product_object() -> Product:
    return Product(
        "1", 
        "Chocotone", 
        "Bauducco", 
        "01-12-2023", 
        "01-05-2024", 
        "12345678", 
        "Keep it away from the sun")

def test_product_report(product_object, capsys) -> None:
    print(product_object)
    captured = capsys.readouterr()
    assert captured.out == (
            f"The product 1 - Chocotone "
            f"with serial number 12345678 "
            f"manufactured on 01-12-2023 "
            f"by the company Bauducco "
            f"valid until 01-05-2024 "
            "must be stored according to the following instructions: "
            f"Keep it away from the sun.\n"
        )
    assert captured.err == ""
