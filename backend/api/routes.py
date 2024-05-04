from flask import Blueprint, request, jsonify
from services.googleMaps import fetch_route_data
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


api = Blueprint('api', __name__)

@api.route('/calculate-route', methods=['POST'])
def calculate_route():
    logger.debug("Received request to /api/calculate-route")
    try:
        data = request.get_json()
        logger.debug(f"Request data: {data}")
        start = data['start']
        end = data['end']
        route_data = fetch_route_data(start, end)
        return jsonify(route_data), 200
    except Exception as e:
        logger.error("An error occurred: ", exc_info=True)
        return jsonify({'error': str(e)}), 500
