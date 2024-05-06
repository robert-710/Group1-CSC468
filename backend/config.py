import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

    # Add database configuration for PostgreSQL
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    DB_NAME = os.environ.get('DB_NAME', 'your_database_name')
    DB_USER = os.environ.get('DB_USER', 'your_username')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_password')

    if not GOOGLE_MAPS_API_KEY:
        raise ValueError("No Google Maps API key set!")
