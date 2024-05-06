import requests
from flask import current_app as app
from shapely.geometry import Point, LineString
from geopy.distance import geodesic

def fetch_route_data(start_address, end_address):
    api_key = app.config['GOOGLE_MAPS_API_KEY']
    # Convert addresses to coordinates
    start_coords = geocode_address(start_address, api_key)
    end_coords = geocode_address(end_address, api_key)

    waypoints = get_scenic_waypoints(start_coords, end_coords)
    waypoints_str = '|'.join(['via:' + waypoint for waypoint in waypoints])
    directions_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_coords}&destination={end_coords}&waypoints={waypoints_str}&key={api_key}"

    response = requests.get(directions_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch directions: {response.text}")

def geocode_address(address, api_key):
    """ Convert address to latitude and longitude """
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    # "https://maps.googleapis.com/maps/api/js?key=AIzaSyCyUvERM7_630MiUUvVIYQVbYJxxN2xSNE&libraries=places,directions&callback=initMap" 
    app.logger.debug(f"Geocoding url: {geocode_url}")
    response = requests.get(geocode_url)
    response.raise_for_status()  # Ensure we raise exceptions for network errors

    data = response.json()
    if not data['results']:
        raise ValueError(f"No geocoding results for address: {address}")

    result = data['results'][0]['geometry']['location']
    return f"{result['lat']},{result['lng']}"

def get_scenic_waypoints(start, end, max_detour_distance=1000):
    # Hard-coded dummy scenic waypoints around Philadelphia
    scenic_locations = [
    {'latitude': 39.952956, 'longitude': -75.647630},  # Stroud Preserve
    {'latitude': 39.95857345998028, 'longitude': -75.60791307826325},  # Chester County Justice Center
    {'latitude': 39.94744696089575, 'longitude': -75.6039600717412},  # Hicksite Friends Cemetery
    {'latitude': 39.951958788686895, 'longitude': -75.5964952739565},  # West Chester Fountain
    {'latitude': 39.95337127409166, 'longitude': -75.59809937044906},  # Emile K. Asplundh Concert Hall
    {'latitude': 39.9371173782603, 'longitude': -75.60150680516085},  # Farrell Stadium
    {'latitude': 39.93517163704869, 'longitude': -75.59934513473529},  # Robert B. Gordon Natural Trail 1
    {'latitude': 39.93428882880664, 'longitude': -75.60294008680106},  # Robert B. Gordon Natural Trail 2
    {'latitude': 39.95375223144274, 'longitude': -75.611264035319},  # Everhart Park
    {'latitude': 39.957605958741745, 'longitude': -75.60568393543818},  # First Presbyterian Church
    {'latitude': 39.957475264631306, 'longitude': -75.60238819040379},  # Church of the Holy Trinity
    {'latitude': 39.96012179311294, 'longitude': -75.60575047439467},  # Sedona Taphouse
    {'latitude': 39.959265651216256, 'longitude': -75.60860994394778},  # Saint Agnes Parish
    {'latitude': 39.9611003796931, 'longitude': -75.60567619465621},  # Hotel Warner
    {'latitude': 39.96195895437786, 'longitude': -75.60592956395075},  # Chester County History Center
    {'latitude': 39.9619831208516, 'longitude': -75.60666395203283},  # Uptown Knauer Performing Arts Center
    {'latitude': 39.95973030972267, 'longitude': -75.60447749448159},  # Downtown West Chester
    {'latitude': 39.95993485286808, 'longitude': -75.60478602398717},  # Historic Chester County Courthouse
    {'latitude': 39.96019773924854, 'longitude': -75.60462719738477},  # Truist
    {'latitude': 39.9660684430755, 'longitude': -75.60405732272866},  # Marshall Square Park
    {'latitude': 39.96359652474387, 'longitude': -75.60867548703663},  # West Chester Public Library
    {'latitude': 39.9647671828922, 'longitude': -75.60903210192576},  # Barclay Park
    {'latitude': 39.96688694999501, 'longitude': -75.6126136530107},  # West Chester Golf and Country Club
    {'latitude': 39.963141731783814, 'longitude': -75.62031764938492},  # Hoopes Park
    {'latitude': 39.95922341106605, 'longitude': -75.61153283796267},  # Beermill
    {'latitude': 39.94649169348807, 'longitude': -75.61423731613569},  # Antique Ice Tool Museum
    {'latitude': 39.94148705632282, 'longitude': -75.621059696716},  # Mt Bradford Preserve
    {'latitude': 39.93676473829113, 'longitude': -75.62406101812701},  # Sconnelltown Park
    {'latitude': 39.92374538998532, 'longitude': -75.5672337388393},  # West Town Amish Market
    {'latitude': 39.908691307832406, 'longitude': -75.59181035962604},  # Thornburry Farm CSA
    {'latitude': 39.94471749230372, 'longitude': -75.62489234232946},  # Grand Slam Equestrian LLC
    {'latitude': 39.96821150254589, 'longitude': -75.64291700776471},  # Timber Top Farm Trail
    {'latitude': 39.97610062253412, 'longitude': -75.64006984309417},  # Abernethy Forest Preserve
    {'latitude': 39.96322431966151, 'longitude': -75.6540817023538},  # Brandywine Park
    {'latitude': 39.96312982780873, 'longitude': -75.65753647614827},  # Ingram's Mill Nature Area
]

    
    # Parse the start and end coordinate strings
    start_lat, start_lng = map(float, start.split(','))
    end_lat, end_lng = map(float, end.split(','))

    # Create shapely Points for start and end
    start_point = Point(start_lng, start_lat)
    end_point = Point(end_lng, end_lat)

    # Create a LineString from start to end
    route_line = LineString([start_point, end_point])

    # Filter locations that are within the specified max_detour_distance from the route
    nearby_scenic_locations = [
        location for location in scenic_locations
        if is_location_near_route(route_line, Point(location['longitude'], location['latitude']), max_detour_distance)
    ]

    # Convert nearby scenic locations to waypoints
    waypoints = [f"{location['latitude']},{location['longitude']}" for location in nearby_scenic_locations]

    return waypoints

def is_location_near_route(route_line, location_point, max_detour_distance):
    closest_point = route_line.interpolate(route_line.project(location_point))
    distance = geodesic((closest_point.y, closest_point.x), (location_point.y, location_point.x)).meters
    return distance <= max_detour_distance
