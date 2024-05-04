# Use the official PostgreSQL image with PostGIS extension
FROM postgis/postgis:13-3.1

# Set environment variables
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=database

# Expose the PostgreSQL port
EXPOSE 5432

# Copy the CSV file to the container
COPY Scenic_Locations.csv /tmp/Scenic_Locations.csv

# Copy the SQL script to create table and import data
COPY init.sql /docker-entrypoint-initdb.d/
