import api.services.vehicles as service

# This module contains all functions to controll requests

# @description: Function to handle /metrobuses requests
# @return: the response from the service
def get_available_vehicles():    
    service_response = service.get_vehicles()
    return service_response 


# @description: Function to control data received from /metrobuses/<id> requests
# @return: the response from the service
def get_vehicle_address_by_id(id):
    if type(id) == 'str' or id < 0:
        return 'Not found, invalid id'
    else:
        service_response = service.get_vehicle(id)
        return service_response