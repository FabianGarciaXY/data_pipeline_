-- Creating vehicles table for vehicles_db that will contain data fetched from metrobuses API of CDMX open data
CREATE TABLE IF NOT EXISTS vehicles (
  id SERIAL PRIMARY KEY ,
  date_updated VARCHAR(22) NOT NULL,
  vehicle_id SMALLINT NOT NULL,
  vehicle_label SMALLINT NOT NULL,
  vehicle_current_status VARCHAR(2) NOT NULL,
  vehicle_latitude FLOAT NOT NULL DEFAULT 0,
  vehicle_longitude FLOAT NOT NULL DEFAULT 0,
  geographic_point VARCHAR(40) NOT NULL,
  position_speed SMALLINT NOT NULL,
  position_odometer SMALLINT NOT NULL,
  trip_schedule_relationship SMALLINT NOT NULL,
  trip_id INTEGER NOT NULL,
  trip_start_date INTEGER NOT NULL DEFAULT 0,
  trip_route_id SMALLINT NOT NULL DEFAULT 0,
  delegation VARCHAR(30) NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);