# This module contains all functions to controll requests

# @description: Function to handle /delegations requests
# @return: the response from the service
def get_available_delegations():
    data = {"test": "test"}
    return data

# @description: Function to control data received from /delegations/<name> requests
# @return: the response from the service
def get_vehicle_by_id(name):
    name = name

    if name == None or not name.isalpha():
        return {"error": "Invalid id"}
    else:
        return # function call