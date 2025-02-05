import enum

# Rarity Enum
class Rarity(enum.Enum):
    COMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4

class Item:
    def __init__(self, name: str, price: int, rarity: Rarity):
        self.name = name
        self.price = price
        self.rarity = rarity

    def __str__(self):
        return f"{self.name}"