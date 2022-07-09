from psycopg2 import extras
from graphql_api.utils.db import connect_db

# This module contains functions to access to data according with bussiness rules

# @description: Function to access to delegations data
# @return: the response from the database to the controller
def get_delegations():
    try:
        connection = connect_db()
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            # Executing query
            query = "SELECT DISTINCT delegation FROM vehicles WHERE delegation != 'Not available';"
            cursor.execute(query)
            response = cursor.fetchall()
            cursor.close()
            connection.close()
        return response
            
    except Exception as err:
        raise err


# @description: Function to access to available vehicles given a delegation name
# @return: the response from the database
def get_vehicles(name):
    try:
        connection = connect_db()
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            # Executing query
            query = 'SELECT * FROM vehicles WHERE delegation = %s AND trip_id IS NOT NULL;'
            cursor.execute(query, (name, ))
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            
        if response == []:
            return {'message': 'This delegation does not exits'}
        else: 
            return response
            
    except Exception as err:
        raise err