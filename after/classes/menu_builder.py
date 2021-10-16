from typing import List, TypeVar, Union

from tabulate import tabulate
from enum import Enum, auto

from after.models.product import Product, ProductCategory


class ProductProperty(Enum):
    NAME = auto()
    PRICE = auto()
    CATEGORY = auto()
    DISCOUNTABLE = auto()


class MenuBuilder:
    def __init__(self, products: List[Product]):
        """Class responsible for displaying the inventory in a specified table format."""

        self.products = products
        self.name_column = [product.name for product in self.products]
        self.price_column = [product.price for product in self.products]
        self.category_column = [product.category.value for product in self.products]
        self.discountable_column = [product.discountable for product in self.products]

    def get_default(self):
        columns = {
            "ITEM": self.name_column,
            "PRICE (S$)": self.price_column,
            "CATEGORY": self.category_column,
            "DISCOUNTABLE": self.discountable_column
        }

        return tabulate(columns, headers="keys", tablefmt="fancy_grid")

    def get_property_sorting(self, prop: ProductProperty, descending: bool = False) -> \
            Union[List[str], List[float], List[ProductCategory], List[bool]]:
        """Get sorting of specified property in ascending or descending order."""
        property_sortings = []

        if prop == ProductProperty.PRICE:
            property_sortings = [product.price for product in self.products]

        elif prop == ProductProperty.NAME:
            property_sortings = [product.name for product in self.products]

        elif prop == ProductProperty.CATEGORY:
            property_sortings = [product.category.value for product in self.products]

        elif prop == ProductProperty.DISCOUNTABLE:
            property_sortings = [product.discountable for product in self.products]

        property_sortings.sort(reverse=descending)
        return property_sortings
