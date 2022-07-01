# Importing function to get credentials and modules to connect to database
from psycopg2 import connect
from sqlalchemy import create_engine
from api.config.config import get_credentials

# This module contains configuration for connecting to db.

# @description: Function to connect aws database(postgres)
# @returns: connection with pycopg2
def connect_db():
    try:
        conf = get_credentials()
        connection = connect(
            host=conf["host"],
            port=conf["port"],
            dbname=conf["dbname"],
            user=conf["user"],
            password=conf["password"],
        )
        return connection

    except Exception as err:
        raise err



# @description: Function to connect aws database(postgres)
# @returns: connection with sqlalchemy
def get_engine():
    try:
        conf = get_credentials()
        engine = create_engine(
            "postgresql://{}:{}@{}:{}/{}".format(
                conf["user"],
                conf["password"],
                conf["host"],
                conf["port"],
                conf["dbname"],
            )
        )
        return engine

    except Exception as err:
        raise err

