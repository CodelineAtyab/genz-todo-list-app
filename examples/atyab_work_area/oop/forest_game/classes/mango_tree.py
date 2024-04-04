from tree import Tree
from mango import Mango


class MangoTree(Tree):
    def __init__(self):
        self.list_of_mangoes: list[Mango] = []
