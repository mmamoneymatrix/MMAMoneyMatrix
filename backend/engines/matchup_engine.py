import numpy as np

class MatchupEngine:
    def __init__(self, fighter_a, fighter_b):
        self.f1 = fighter_a
        self.f2 = fighter_b

    def generate_fight_geometry(self):
        """
        Creates a 'Fight Geometry Object' describing advantages and modifiers.
        """
        geometry = {
            "range_control": self._calculate_range_control(),
            "pace_control": self._calculate_pace_control(),
            "grappling_advantage": self._calculate_grappling_advantage(),
            "striking_advantage": self._calculate_striking_advantage(),
            "chaos_factor": self._calculate_chaos_factor(),
            "cardio_advantage": self._calculate_cardio_advantage(),
            "early_round_advantage": self._calculate_round_advantage("early"),
            "late_round_advantage": self._calculate_round_advantage("late"),
            "finish_threat": self._calculate_finish_threat(),
            "vulnerability": self._calculate_vulnerability(),
            "gym_tier_modifier": self._get_gym_modifier(),
            "context_modifier": self._get_context_modifier()
        }
        return geometry

    def _calculate_range_control(self):
        # Reach and height differential + striking accuracy
        reach_diff = self.f1.get('reach', 0) - self.f2.get('reach', 0)
        acc_diff = self.f1.get('striking_accuracy', 0) - self.f2.get('striking_accuracy', 0)
        return (reach_diff * 0.6) + (acc_diff * 0.4)

    def _calculate_pace_control(self):
        # SLpM vs SApM
        f1_pace = self.f1.get('slpm', 0) - self.f1.get('sapm', 0)
        f2_pace = self.f2.get('slpm', 0) - self.f2.get('sapm', 0)
        return f1_pace - f2_pace

    def _calculate_grappling_advantage(self):
        # TD average, TD accuracy, Sub average vs TD defense
        f1_grappling = (self.f1.get('td_avg', 0) * self.f1.get('td_acc', 0)) + self.f1.get('sub_avg', 0)
        f2_defense = self.f2.get('td_def', 0)
        return f1_grappling - (f2_defense / 100.0)

    def _calculate_striking_advantage(self):
        return self.f1.get('striking_accuracy', 0) - self.f2.get('striking_accuracy', 0)

    def _calculate_chaos_factor(self):
        # High variance fighters
        return (self.f1.get('knockdown_avg', 0) + self.f2.get('knockdown_avg', 0)) / 2.0

    def _calculate_cardio_advantage(self):
        return self.f1.get('cardio_index', 50) - self.f2.get('cardio_index', 50)

    def _calculate_round_advantage(self, stage):
        if stage == "early":
            return self.f1.get('early_round_rating', 50) - self.f2.get('early_round_rating', 50)
        return self.f1.get('late_round_rating', 50) - self.f2.get('late_round_rating', 50)

    def _calculate_finish_threat(self):
        return self.f1.get('finish_rate', 0.5)

    def _calculate_vulnerability(self):
        return self.f2.get('damage_tolerance', 50)

    def _get_gym_modifier(self):
        # Placeholder for gym tier logic
        return 1.0

    def _get_context_modifier(self):
        # Placeholder for short notice, altitude, etc.
        return 1.0
