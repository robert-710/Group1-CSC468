import requests
from flask import current_app as app
from models.scenicLocation import ScenicLocation
from shapely.geometry import Point, LineString
from geopy.distance import geodesic

def fetch_route_data(start, end):
    api_key = app.config['GOOGLE_MAPS_API_KEY']
    waypoints = get_scenic_waypoints(start, end)
    waypoints_str = '|'.join(waypoints)
    directions_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={end}&waypoints={waypoints_str}&key={api_key}"

    response = requests.get(directions_url)
    response.raise_for_status()
    return response.json()

# Helper function to check if a point is near the route
def is_location_near_route(route_line, location_point, max_detour_distance):
    closest_point = route_line.interpolate(route_line.project(location_point))
    distance = geodesic((closest_point.y, closest_point.x), (location_point.y, location_point.x)).meters
    return distance <= max_detour_distance

# Main function to get scenic waypoints
def get_scenic_waypoints(start, end, max_detour_distance=10000):
    # Convert the start and end coordinates into shapely Points
    start_point = Point(start['longitude'], start['latitude'])
    end_point = Point(end['longitude'], end['latitude'])

    # Create a LineString from start to end
    route_line = LineString([start_point, end_point])

    # Get all scenic locations from the database (mocked for this example)
    scenic_locations = ScenicLocation.get_all_scenic_locations()

    # Filter locations that are within the specified max_detour_distance from the route
    nearby_scenic_locations = [
        location for location in scenic_locations
        if is_location_near_route(route_line, Point(location.longitude, location.latitude), max_detour_distance)
    ]

    # Convert nearby scenic locations to waypoints
    waypoints = [f"{location.latitude},{location.longitude}" for location in nearby_scenic_locations]

    return waypoints
