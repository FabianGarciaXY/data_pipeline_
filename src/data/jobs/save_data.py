# Importing db connection, dataframe and functions to get data
from api.database.db import get_engine, connect_db
from data.transformations.dataframe import create_dataframe
from data.resources.inputs.reader import fetch_vehicles_data, get_location

# Module to save data into the aws postgres database

# @description: Function to save data in db.
# @params {string, pandas object, funtion, function}: 
# - The database connection with sqlalchemy defined in db module
# - The pandas dataframe conaining the vehicles data
# - The function to fetch data from the vehicles API
# - The function to get the location of the vehicles
def save_data(conn, engine, dataframe, data, location):

    try:
        #Gettin connections
        conn = conn()
        engine = engine()

        # Getting dataframe and saving it
        df = dataframe(data, location)
        df.to_sql('vehicles', con=engine, schema='public', if_exists='append', index=False)
        
        conn.commit()
        conn.close()

    except Exception as err:
        raise err


# Calling the save_data function
save_data(connect_db, get_engine, create_dataframe, fetch_vehicles_data, get_location)