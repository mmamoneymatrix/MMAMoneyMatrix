from flask import Blueprint, request, jsonify

get_fighter_bp = Blueprint('get_fighter', __name__)

@get_fighter_bp.route('/get-fighter/<int:fighter_id>', methods=['GET'])
def get_fighter(fighter_id):
    # Fetch from DB
    return jsonify({"id": fighter_id, "name": "Sample Fighter", "stats": {}})
