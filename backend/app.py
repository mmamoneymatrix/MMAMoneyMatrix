from flask import Flask
from flask_cors import CORS
from routes.import_fighter import import_fighter_bp
from routes.run_simulation import run_simulation_bp
from routes.get_fighter import get_fighter_bp
from routes.get_history import get_history_bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(import_fighter_bp, url_prefix='/api')
app.register_blueprint(run_simulation_bp, url_prefix='/api')
app.register_blueprint(get_fighter_bp, url_prefix='/api')
app.register_blueprint(get_history_bp, url_prefix='/api')

@app.route('/')
def index():
    return {"status": "MMAMoneyMatrix Backend Running"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
