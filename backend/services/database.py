import psycopg2
from flask import current_app as app

def get_db_connection():
    conn = psycopg2.connect(
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        database=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD']
    )
    return conn

def get_scenic_locations():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, ST_AsText(coordinate) AS coordinate FROM scenic_locations")
    scenic_locations = []
    for name, coordinate in cur.fetchall():
        lat, lng = coordinate.split('(')[1].split(')')[0].split()
        scenic_locations.append({'name': name, 'latitude': float(lat), 'longitude': float(lng)})
    cur.close()
    conn.close()
    return scenic_locations
