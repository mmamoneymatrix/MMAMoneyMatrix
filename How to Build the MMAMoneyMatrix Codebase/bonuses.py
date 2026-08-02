class BonusLayer:
    def __init__(self):
        self.gym_tiers = {
            "S": (0.04, 0.07),
            "A": (0.02, 0.03),
            "B": (-0.01, -0.03),
            "C": (0.0, 0.0)
        }
        
        self.underdog_bonuses = {
            "mild": 0.03,
            "medium": 0.05,
            "strong": 0.06,
            "heavy": 0.07
        }

    def apply_gym_bonus(self, win_prob, tier):
        bonus_range = self.gym_tiers.get(tier, (0.0, 0.0))
        # Take mid point for simulation
        bonus = (bonus_range[0] + bonus_range[1]) / 2.0
        return win_prob + (win_prob * bonus)

    def apply_underdog_bonus(self, win_prob, level):
        bonus = self.underdog_bonuses.get(level, 0.0)
        return win_prob + bonus
