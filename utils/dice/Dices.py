import copy
import random
from collections import Counter


class Dice:
    def __init__(self, value: int):
        self.value: int = value

    def __add__(self, other):
        if isinstance(other, Dice):
            return Dices([self, other])
        elif isinstance(other, int):
            dices = [self]
            for i in range(0, other):
                dices.append(Dice(1))
            return Dices(dices)

        TypeError("Can only add with other dice or int")

    def __rmul__(self, other):
        if isinstance(other, int):
            dices = []
            if other == 1:
                return Dices([self])

            for i in range(0, other):
                dices.append(copy.copy(self))
            return Dices(dices)

        TypeError("Can only multiply with other dices")

    def roll(self) -> int:
        if self.value == 1:
            return 1
        return random.randint(1, self.value)


class Dices:
    def __init__(self, dices: list[Dice]):
        self.dices: list[Dice] = dices

    def __add__(self, other):
        if isinstance(other, Dice):
            self.dices.append(other)
        elif isinstance(other, Dices):
            self.dices += other.dices
        elif isinstance(other, int):
            self.__add__(other * Dice(1))

        return self

    def roll(self) -> tuple[str, int]:
        # Count occurrences of each type of dice
        dice_counter = Counter([dice.value for dice in self.dices if dice.value != 1])
        modifier = sum(1 for dice in self.dices if dice.value == 1)

        # Roll the dice and construct the output string
        results = []
        total_sum = 0

        for dice_value, count in sorted(dice_counter.items()):
            if count == 1:  # Single die
                roll_result = Dice(dice_value).roll()
                results.append(f"{roll_result}")
                total_sum += roll_result
            else:  # Multiple dice of the same type
                rolls = [Dice(dice_value).roll() for _ in range(count)]
                rolls_sum = sum(rolls)
                results.append(f"({'+'.join(map(str, rolls))})")
                total_sum += rolls_sum

        # Add modifier at the end if it exists
        if modifier > 0:
            results.append(f"{modifier}")
            total_sum += modifier

        # Construct the final string representation
        result_str = " + ".join(results)
        result_str += f" = {total_sum}"

        return result_str, total_sum

    def dice_text(self) -> str:
        dice_counter = Counter()
        modifier = 0

        for dice in self.dices:
            if dice.value == 1:
                modifier += 1
            else:
                dice_counter[f"d{dice.value}"] += 1

        # Build the result string
        parts = []
        for dice_type, count in sorted(dice_counter.items()):
            if count == 1:
                parts.append(f"1{dice_type}")
            else:
                parts.append(f"{count}{dice_type}")

        if modifier > 0:
            parts.append(f"{modifier}")

        return " + ".join(parts)
