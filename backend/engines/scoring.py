import numpy as np

class ScoringModel:
    def __init__(self):
        # Real UFC judging bias matrices
        self.bias_profiles = {
            "striking_heavy": {"striking": 0.7, "grappling": 0.2, "control": 0.1},
            "grappling_heavy": {"striking": 0.2, "grappling": 0.7, "control": 0.1},
            "control_heavy": {"striking": 0.1, "grappling": 0.2, "control": 0.7},
            "balanced": {"striking": 0.4, "grappling": 0.4, "control": 0.2}
        }

    def score_round(self, f1_stats, f2_stats, bias="balanced"):
        """
        Scores a round based on stats and judge bias.
        """
        profile = self.bias_profiles.get(bias, self.bias_profiles["balanced"])
        
        f1_score = (f1_stats['strikes'] * profile['striking']) + \
                   (f1_stats['takedowns'] * profile['grappling']) + \
                   (f1_stats['control_time'] * profile['control'])
                   
        f2_score = (f2_stats['strikes'] * profile['striking']) + \
                   (f2_stats['takedowns'] * profile['grappling']) + \
                   (f2_stats['control_time'] * profile['control'])
                   
        if f1_score > f2_score * 1.5:
            return (10, 8)
        elif f1_score > f2_score:
            return (10, 9)
        elif f2_score > f1_score * 1.5:
            return (8, 10)
        else:
            return (9, 10)

    def aggregate_scores(self, rounds):
        f1_total = sum([r[0] for r in rounds])
        f2_total = sum([r[1] for r in rounds])
        
        if f1_total > f2_total:
            return "Unanimous Decision - Fighter A"
        elif f2_total > f1_total:
            return "Unanimous Decision - Fighter B"
        else:
            return "Draw"
