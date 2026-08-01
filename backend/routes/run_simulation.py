from flask import Blueprint, request, jsonify
from engines.matchup_engine import MatchupEngine
from engines.monte_carlo import MonteCarloEngine

run_simulation_bp = Blueprint('run_simulation', __name__)

@run_simulation_bp.route('/run-simulation', methods=['POST'])
def run_simulation():
    data = request.json
    fighter_a = data.get('fighter_a')
    fighter_b = data.get('fighter_b')
    iterations = data.get('iterations', 10000)
    
    # 1. Generate Fight Geometry
    engine = MatchupEngine(fighter_a, fighter_b)
    geometry = engine.generate_fight_geometry()
    
    # 2. Run Monte Carlo Simulation
    mc = MonteCarloEngine(geometry, iterations=iterations)
    results = mc.run()
    
    return jsonify({
        "geometry": geometry,
        "results": results
    })
