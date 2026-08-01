from flask import Blueprint, request, jsonify

import_fighter_bp = Blueprint('import_fighter', __name__)

@import_fighter_bp.route('/import-fighter', methods=['POST'])
def import_fighter():
    data = request.json
    # Logic to scrape or ingest data
    # Save to database (Supabase/Postgres)
    return jsonify({"message": "Fighter imported successfully", "fighter": data})
