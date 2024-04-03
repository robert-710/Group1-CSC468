# /backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from kubernetes import client, config
import base64
import os

app = Flask(__name__)
CORS(app)

def get_api_key_from_secret():
    try:
        config.load_incluster_config()
        v1 = client.CoreV1Api()
        namespace = 'roberts3'  # Replace with your namespace
        secret_name = 'api-key'  # Replace if your Secret is named differently
        secret = v1.read_namespaced_secret(secret_name, namespace)
        api_key = base64.b64decode(secret.data['API_KEY']).decode('utf-8')
        return api_key
    except Exception as e:
        print(f"Error fetching API key from Secret: {e}")
        # Exit with error or return default or handle gracefully
        return None

@app.route('/api/key')
def api_key():
    try:
        api_key = get_api_key_from_secret()
        if not api_key:
            return jsonify(error="Error retrieving API key"), 500
        return jsonify(api_key=api_key)
    except Exception as e:
        print(f"Error in /api/key: {e}")
        return jsonify(error="Error retrieving API key"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
