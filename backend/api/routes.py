from flask import Blueprint, jsonify, request
from services.googleMaps import fetch_route_data

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/calculate-route', methods=['POST'])
def calculate_route():
    data = request.get_json()
    start = data.get('start')
    end = data.get('end')

    route_data = fetch_route_data(start, end)
    return jsonify(route_data), 200
