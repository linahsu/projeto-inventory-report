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


def test_create_product() -> None:
    raise NotImplementedError
