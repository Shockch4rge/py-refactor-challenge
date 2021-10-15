from typing import List

from after.models.product import Product
from after.classes.product_manager import ProductManager


class Cart:
    def __init__(self):
        """Responsible for holding a list of products in the inventory"""
        self.manager = ProductManager()
        self.products: List[Product] = []
        self.size = len(self.products)

    def add(self, product_name: str) -> None:
        """Adds an item to the cart by name."""
        found_product = self.manager.find_product_by_name(product_name)

        if not found_product:
            print(f"Item does not exist: {product_name}")

        self.products.append(found_product)

    def remove(self, product_name: str) -> None:
        """Removes an item from the cart by name."""
        found_product = self.manager.find_product_by_name(product_name)
        exists_in_cart = self.check_product_in_cart(product_name)

        if not found_product or not exists_in_cart:
            print(f"Item does not exist: {product_name}")

        self.products.remove(found_product)

    def show(self) -> None:
        """Show all items in the cart."""
        if self.size == 0:
            print("Your cart is empty!")
            return

        for item in self.products:
            print(f"{item.name}\n")

    def clear(self) -> None:
        """Clear all items from the cart."""
        if self.size == 0:
            print("Your cart is already empty!")
            return

        self.products.clear()
        print("Cart cleared!")

    def check_product_in_cart(self, name: str) -> bool:
        """Checks for an item in the cart by name."""
        product_names = [product.name for product in self.products]

        product_count = product_names.count(name)
        print(f"There are {product_count} {name}(s) in the cart!")

        return product_count != 0
