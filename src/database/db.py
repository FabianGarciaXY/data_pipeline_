# Importing os and connect function to connect to database
import os
from psycopg2 import connect


# Excuting connection
def connect_db():
    
    try:
        # Getting credentials from docker-compose environment variables
        host = os.environ['PG_HOST']
        port = os.environ['PG_PORT']
        db = os.environ['PG_DATABASE']
        user = os.environ['PG_USER']
        password = os.environ['PG_PASSWORD']

        # Connecting to the database
        connection = connect(dbname=db, user=user, password=password, host=host, port=port)
        return connection

    except Exception as ex:
        raise ex