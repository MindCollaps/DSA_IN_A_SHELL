from item import Rarity


class Item:
    def __init__(self, name: str, description: str, price: int, rarity: Rarity):
        self.name: str = name
        self.description = description
        self.price: int = price
        self.rarity: Rarity = rarity

    def __str__(self):
        return f"{self.name}"
