from psycopg2 import extras
from api.database.db import connect_db

# This module contains all functions access to data accordint with bussiness rules

# @description: Function to access to metrobuses data
# @return: the response from the database to the controller
def get_vehicles():
    
    try:
        connection = connect_db()
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            query = 'SELECT * FROM vehicles WHERE trip_id IS NOT NULL ORDER BY vehicle_id;'
        	# Executing query
            cursor.execute(query)
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            
        return response
            
    except Exception as err:
    	raise err 


# @description: Function to access to vehicle location data
# @return: the response from the database
def get_vehicle(id):
    
    try:
        connection = connect_db()
        with connection.cursor(cursor_factory=extras.RealDictCursor) as \
            cursor:
            query = 'SELECT vehicle_id, delegation, geographic_point FROM vehicles WHERE vehicle_id = %s;'
            cursor.execute(query, (id, ))
            response = cursor.fetchone()
            cursor.close()
            connection.close()
            
        return response
        
    except Exception as err:
        raise err