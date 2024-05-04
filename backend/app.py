from flask import Flask
from flask_cors import CORS
import os

# Import the Blueprint from routes.py
from api.routes import api

app = Flask(__name__)
CORS(app)

# Load configurations, including the Google Maps API key from environment variables
app.config['GOOGLE_MAPS_API_KEY'] = os.getenv('GOOGLE_MAPS_API_KEY', 'fallback-key-if-env-var-not-set')

# Register the Blueprint
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Scenic Navigation App API!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
