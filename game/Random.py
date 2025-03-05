from item import *
import random
from typing import List
import sys

def getRandomItems(rarity: Rarity, amount: int) -> List[Consumable]:
    from item import Consumable, __all__ as item_all
    item_classes = [getattr(sys.modules['item'], class_name) for class_name in item_all if class_name != 'Rarity' and class_name != 'EffectType']
    
    consumable_classes = [item_class for item_class in item_classes if issubclass(item_class, Consumable)]
    
    consumables = [item_class() for item_class in consumable_classes]

    return random.sample(consumables, min(amount, len(consumables)))