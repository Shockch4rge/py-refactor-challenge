from dataclasses import dataclass
from enum import Enum, auto


class ProductCategory(Enum):
    TABLET = auto()
    LAPTOP = auto()
    GAME_CONSOLE = auto()
    ANY = auto()


@dataclass(frozen=True)
class Product:
    name: str
    price: float
    category: ProductCategory
    discountable: bool
