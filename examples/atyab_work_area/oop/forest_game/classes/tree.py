from abc import ABC
from fruit import Fruit


class Tree(ABC):
    NAME = "I AM A TREE"  # I am a constant, plz dont change me

    def __init__(self):
        self.list_of_fruits: list[Fruit] = []


if __name__ == "__main__":
    Tree.list_of_fruits
