import numpy as np
from .scoring import ScoringModel
from .bonuses import BonusLayer

class MonteCarloEngine:
    def __init__(self, geometry, iterations=10000):
        self.geometry = geometry
        self.iterations = iterations
        self.scoring_model = ScoringModel()
        self.bonus_layer = BonusLayer()

    def run(self):
        results = []
        for _ in range(self.iterations):
            sim_result = self.simulate_fight()
            results.append(sim_result)
        
        return self.aggregate_results(results)

    def simulate_fight(self):
        # Base probabilities derived from geometry
        win_prob = 0.5 + (self.geometry['striking_advantage'] * 0.01) + (self.geometry['grappling_advantage'] * 0.05)
        win_prob += (self.geometry['cardio_advantage'] * 0.002)
        
        # Apply bonuses
        win_prob = self.bonus_layer.apply_gym_bonus(win_prob, self.geometry['gym_tier_modifier'])
        
        # Determine outcome
        roll = np.random.random()
        
        if roll < win_prob:
            winner = "fighter_a"
        else:
            winner = "fighter_b"
            
        # Determine method
        method_roll = np.random.random()
        if method_roll < 0.3:
            method = "KO/TKO"
            round_won = np.random.randint(1, 4) # Simplified 3 rounder
        elif method_roll < 0.5:
            method = "Submission"
            round_won = np.random.randint(1, 4)
        else:
            method = "Decision"
            round_won = 3
            
        return {
            "winner": winner,
            "method": method,
            "round": round_won
        }

    def aggregate_results(self, results):
        total = len(results)
        f1_wins = len([r for r in results if r['winner'] == 'fighter_a'])
        f2_wins = total - f1_wins
        
        methods = {}
        for r in results:
            m = r['method']
            methods[m] = methods.get(m, 0) + 1
            
        rounds = {}
        for r in results:
            rd = r['round']
            rounds[rd] = rounds.get(rd, 0) + 1
            
        return {
            "win_probability": f1_wins / total,
            "method_probabilities": {k: v / total for k, v in methods.items()},
            "round_probabilities": {k: v / total for k, v in rounds.items()},
            "iterations": total
        }
