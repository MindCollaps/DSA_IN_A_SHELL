class LevelSystem:
    XP_BASE = 100  # Basis-XP für Level 1

    @staticmethod
    def xp_for_level(level: int) -> int:
        return LevelSystem.XP_BASE * (level ** 2)
