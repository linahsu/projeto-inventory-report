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


def test_create_product(product_object) -> None:
    """Testa se o construtor do objeto Product contém os atributos corretos."""
    
    assert product_object.id == "1"
    assert product_object.product_name == "Chocotone"
    assert product_object.company_name == "Bauducco"
    assert product_object.manufacturing_date == "01-12-2023"
    assert product_object.expiration_date == "01-05-2024"
    assert product_object.serial_number == "12345678"
    assert product_object.storage_instructions == "Keep it away from the sun"
