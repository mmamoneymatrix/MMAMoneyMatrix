from flask import Blueprint, request, jsonify

get_history_bp = Blueprint('get_history', __name__)

@get_history_bp.route('/get-history/<int:fighter_id>', methods=['GET'])
def get_history(fighter_id):
    # Fetch fight history from DB
    return jsonify({"fighter_id": fighter_id, "history": []})
