from tabulate import tabulate
from enum import Enum, auto


class SortOrder(Enum):
    ASCENDING: auto()
    ALPHABETICAL: auto()
    CATEGORY: auto()


class Menu:
    def __init__(self):
        pass

    def sort(self, order: SortOrder):
        pass

    def show(self):
        pass
