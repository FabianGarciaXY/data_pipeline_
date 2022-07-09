from psycopg2 import extras
from graphql_api.utils.db import connect_db

# This module contains all functions access to data according with bussiness rules

# @description: Function to access to metrobuses data
# @return: the response from the database to the controller
def get_vehicles():
    try:
        connection = connect_db()
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            # Executing query
            query = 'SELECT * FROM vehicles WHERE trip_id IS NOT NULL ORDER BY vehicle_id;'
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
            query = 'SELECT * FROM vehicles WHERE vehicle_id = %s;'
            cursor.execute(query, (id, ))
            response = cursor.fetchone()
            cursor.close()
            connection.close()
            
        if response is None:
            return {'error' : 'vehicle with this id does not exist'}

        return response
        
    except Exception as err:
        raise err