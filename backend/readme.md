# Scenic Navigation App

## Description
The Scenic Navigation App is a Flask-based application designed to help users find the most scenic routes between two points. This application integrates with the Google Maps API to generate routes that include designated scenic locations stored in a static database.

## Features
- Calculate routes that include scenic waypoints.
- Integration with Google Maps API for route mapping.
- Flask backend with a PostgreSQL database for storing scenic location data.

## Prerequisites
- Python 3.12
- Docker
- A Google Maps API key

## Local Development Setup

### Setting Up the Python Environment
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scenic-navigation-app.git
   cd scenic-navigation-app
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Setting Up the Database
TODO: instructions about setting up the database

### Environment Variables
Create a `.env` file in the project root directory and add the following:
```plaintext
GOOGLE_MAPS_API_KEY='YourGoogleMapsAPIKeyHere'
```

## Running Locally Without Docker
To run the Flask application locally without Docker:
```bash
python app.py
```
The application will be available at `http://localhost:5000`.

## Running with Docker
To build the Docker container and run the application:
```bash
docker build -t scenic-navigation-app .
docker run -p 5000:5000 scenic-navigation-app
```
The application will be available at `http://localhost:5000`.

## Testing
```bash
python -m pytest
```
