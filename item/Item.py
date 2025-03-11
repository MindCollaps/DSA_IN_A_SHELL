from item import Rarity


class Item:
    def __init__(self, name: str, description: str, price: int, rarity: Rarity):
        self.name = name
        self.description = description
        self.price = price
        self.rarity = rarity

    def __str__(self):
        return f"{self.name}"
