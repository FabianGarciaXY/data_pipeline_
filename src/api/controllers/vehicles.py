# This module contains all functions to controll requests

# @description: Function to handle /metrobuses requests
# @return: the response from the service
def get_all_vehicles():
    data = {"test": "test"}
    return data

# @description: Function to control data received from /metrobuses/<id> requests
# @return: the response from the service
def get_vehicle_by_id(id):
    data = id

    if id < 0 or type(id) != int:
        return {"error": "Invalid id"}
    else:
        return # function call