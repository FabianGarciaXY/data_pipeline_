import api.services.delegation as service

# This module contains all functions to controll requests

# @description: Function to handle /delegations requests
# @return: the response from the service
def get_available_delegations():
    service_response = service.get_delegations()
    return service_response


# @description: Function to control data received from /delegations/<name> requests
# @return: the response from the service
def get_vehicles_by_delegation(name):
    if len(name) < 1 or isinstance(name, str) is False:
        service_response = {'error' : 'enter a valid name' }
    else:
        service_response = service.get_vehicles(name)
        
    return service_response