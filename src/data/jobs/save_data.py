# Importing db connection, dataframe and functions to get data
from api.utils.db import connect_db, get_engine
from data.transformations.clean_data import df

# Module to save data into the aws postgres database

# @description: Function to save data in db.
# @params {string, string, pandas dataframe}: 
# - The database connection string with pycopg2
# - The database connection string sqlalchemy
# - The pandas dataframe conaining the vehicles data
def save_data(conn, engine, dataframe):
    try:
        #Gettin connections
        conn = conn()
        engine = engine()
        
        # Getting dataframe and saving it into the database
        dataframe.to_sql('vehicles', con=engine, schema='public', if_exists='append', index=False)
        conn.commit()
        conn.close()

    except Exception as err:
        raise err


# Calling the save_data function
save_data(connect_db, get_engine, df)