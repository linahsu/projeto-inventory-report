from dataclasses import dataclass


@dataclass
class Product:
    id: str
    product_name: str
    company_name: str
    manufacturing_date: str
    expiration_date: str
    serial_number: str
    storage_instructions: str

    def __str__(self) -> str:
        return (
            f"The product {self.id} - {self.product_name} "
            f"with serial number {self.serial_number} "
            f"manufactured on {self.manufacturing_date} "
            f"by the company {self.company_name} "
            f"valid until {self.expiration_date} "
            "must be stored according to the following instructions: "
            f"{self.storage_instructions}."
        )
if __name__ == "__main__":
    print(Product(
        "1", 
        "Chocotone", 
        "Bauducco", 
        "01-12-2023", 
        "01-05-2024", 
        "12345678", 
        "Manter em lugar arejado e longe do sol"
    ))
