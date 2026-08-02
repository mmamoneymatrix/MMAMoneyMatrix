from flask import Blueprint, request, jsonify
from engines.matchup_engine import MatchupEngine
from engines.monte_carlo import MonteCarloEngine
from models.fighter import Fighter
from models.fight import Fight
from database.db import get_fighter_by_name

run_simulation_bp = Blueprint('run_simulation', __name__)

@run_simulation_bp.route('/run-simulation', methods=['POST'])
def run_simulation():
    data = request.json
    fighter_a_name = data.get('fighter_a')
    fighter_b_name = data.get('fighter_b')
    iterations = data.get('iterations', 10000)

    # 1. Load fighter objects from database
    fighter_a = get_fighter_by_name(fighter_a_name)
    fighter_b = get_fighter_by_name(fighter_b_name)

    if not fighter_a or not fighter_b:
        return jsonify({"error": "One or both fighters not found"}), 400

    # 2. Build matchup engine
    engine = MatchupEngine(fighter_a, fighter_b)
    geometry = engine.generate_fight_geometry()

    # 3. Run Monte Carlo simulation
    mc = MonteCarloEngine(geometry, iterations=iterations)
    results = mc.run()

    return jsonify({
        "geometry": geometry,
        "results": results
    })

