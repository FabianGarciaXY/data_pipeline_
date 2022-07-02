from distutils.debug import DEBUG
import os

# @description: Function to get env variables
# @return: { dictionary } a dictionary with the environment variables
def secrets():
    env_vars = {
        'host': os.environ['AWS_PG_HOST'],
        'port': os.environ['AWS_PG_PORT'],
        'dbname': os.environ['AWS_PG_DATABASE'],
        'user': os.environ['AWS_PG_USER'],
        'password': os.environ['AWS_PG_PASS']
        }
    return env_vars