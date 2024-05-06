-- Create the table
CREATE TABLE scenic_locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  coordinate GEOMETRY(Point, 4326)
);

-- Import data from CSV
COPY scenic_locations (name, coordinate)
FROM '/tmp/Scenic_Locations.csv'
WITH (
  FORMAT CSV,
  HEADER TRUE,
  DELIMITER ',',
  QUOTE '"',
  ENCODING 'UTF8'
);

-- Create spatial index
CREATE INDEX idx_scenic_locations_coordinate ON scenic_locations USING GIST (coordinate);
