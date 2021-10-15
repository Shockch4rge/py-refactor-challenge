from typing import List, Optional

from after.models.product import Product, ProductCategory


class ProductManager:
    """Keeps track of the product inventory and is responsible for product creation."""

    def __init__(self):
        self.products: List[Product] = []

        self.add_product(Product("APPLE MACBOOK AIR", 1345.00, ProductCategory.LAPTOP, True))
        self.add_product(Product("ASUS S533EQ 15.6", 1448.00, ProductCategory.LAPTOP, True))
        self.add_product(Product("LENOVO IP 3", 1308.00, ProductCategory.LAPTOP, True))
        self.add_product(Product("SAMSUNG 64GB GALAXY TAB", 372.00, ProductCategory.TABLET, True))
        self.add_product(Product("APPLE 10.2-INCH IPAD", 456.00, ProductCategory.TABLET, True))
        self.add_product(Product("HUAWEI HW-BAH3 LTE", 372.00, ProductCategory.TABLET, True))
        self.add_product(Product("NINTENDO SWITCH CONSOLE", 457.00, ProductCategory.GAME_CONSOLE, True))
        self.add_product(Product("SONY PLAYSTATION 5", 560.00, ProductCategory.GAME_CONSOLE, True))
        self.add_product(Product("MICROSOFT XBOX CONSOLE", 653.00, ProductCategory.GAME_CONSOLE, True))

    def add_product(self, product: Product) -> None:
        """Append a product to the inventory."""
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """Remove a product from the inventory."""
        self.products.remove(product)

    def get_products(self) -> List[Product]:
        """Get all products in the inventory."""
        return self.products

    def find_product_by_name(self, name: str) -> Optional[Product]:
        """Search for a product in the inventory by name."""
        product_names = [product.name for product in self.products]

        if name not in product_names:
            return None

        for product in self.products:
            if product.name == name:
                return product

    @staticmethod
    def get_empty_product() -> Product:
        """Retrieve an empty product with falsy values."""
        return Product("", 0.0, ProductCategory.ANY, False)
