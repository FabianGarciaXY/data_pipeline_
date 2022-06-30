# Importing os and connect function to connect to database
import os
from psycopg2 import connect
from sqlalchemy import create_engine


#This module contains configuration for connecting to db.


# @description: Function to connect aws database(postgres)
# @returns: connection with pycopg2
def connect_db():
    # Getting credentials from docker-compose environment variables.
    host = os.environ['AWS_PG_HOST']
    port = os.environ['AWS_PG_PORT']
    dbname = os.environ['AWS_PG_DATABASE']
    user = os.environ['AWS_PG_USER']
    password = os.environ['AWS_PG_PASS']

    try:
        # Connection with psycopg2
        connection = connect(host=host, port=port, dbname=dbname, user=user, password=password)

    except Exception as err:
        raise err

    return connection


# @description: Function to connect aws database(postgres)
# @returns: connection with sqlalchemy
def get_engine():
    # Getting credentials from docker-compose environment variables.
    host = os.environ['AWS_PG_HOST']
    port = os.environ['AWS_PG_PORT']
    dbname = os.environ['AWS_PG_DATABASE']
    user = os.environ['AWS_PG_USER']
    password = os.environ['AWS_PG_PASS']

    try: 
        # Connection with sqlalchemy
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
    except Exception as err:
        raise err

    return engine