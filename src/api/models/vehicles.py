from api.database.db import connect_db

# @Desc: Function to create the data table model
# @param: {object} receives the connection with pycopg2.
# As result creates a new table based on vehicle data.
def create_table(connection):
    # Getting the engine and connection
    conn = connection()
    try: 
        curr = conn.cursor()
        curr.execute('DROP TABLE IF EXISTS vehicles;')
        curr.execute('CREATE TABLE IF NOT EXISTS vehicles( \
                      id SERIAL PRIMARY KEY , \
                      date_updated VARCHAR(22) NOT NULL, \
                      vehicle_id SMALLINT NOT NULL, \
                      vehicle_label SMALLINT NOT NULL, \
                      vehicle_current_status VARCHAR(2) NOT NULL, \
                      position_latitude FLOAT NOT NULL DEFAULT 0, \
                      position_longitude FLOAT NOT NULL DEFAULT 0, \
                      geographic_point VARCHAR(40) NOT NULL, \
                      position_speed SMALLINT NOT NULL, \
                      position_odometer SMALLINT NOT NULL, \
                      trip_schedule_relationship SMALLINT NOT NULL, \
                      trip_id INTEGER DEFAULT 0, \
                      trip_start_date INTEGER DEFAULT 0, \
                      trip_route_id SMALLINT DEFAULT 0, \
                      delegation VARCHAR(30) NULL, \
                      created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);')
        conn.commit()
        conn.close()
        
    except Exception as err:
        raise err

# Calling create_table function to create the vehicles table
create_table(connect_db)