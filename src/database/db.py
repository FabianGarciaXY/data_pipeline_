# Importing os and connect function to connect to database
import os
from psycopg2 import connect


# Excuting connection
def connect_db():
    try:
        # Getting credentials from docker-compose environment variables for connecting to the database
        connection = connect(host = os.environ['AWS_PG_HOST'],
                             port = os.environ['AWS_PG_PORT'],
                             dbname = os.environ['AWS_PG_DATABASE'],
                             user = os.environ['AWS_PG_USER'],
                             password = os.environ['AWS_PG_PASS'])
                             
        return connection
        
    except Exception as ex:
        raise ex