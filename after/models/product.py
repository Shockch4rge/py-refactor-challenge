from dataclasses import dataclass
from enum import Enum, auto


class ProductCategory(Enum):
    TABLET = "TABLET"
    LAPTOP = "LAPTOP"
    GAME_CONSOLE = "GAME CONSOLE"
    ANY = ""


@dataclass(frozen=True)
class Product:
    name: str
    price: float
    category: ProductCategory
    discountable: bool
