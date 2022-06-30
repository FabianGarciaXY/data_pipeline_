import requests
import os

# Module to get data from the vehicles API,
# and their locations trough the geocoder API from Google


# @description: Function for fething vehicle data from the API
# @returns: a list of objects containing the vehicles dada
def fetch_vehicles_data():
    
    try:
        # Calling the API
        vehicles_api = os.environ['VEHICLES_API']
        response = requests.get(vehicles_api).json() 
        data = response['result']['records']
        return data

    except Exception as err:
        raise err


# @description: Function for get address of th vehicles
# @param: [String] receives a string containing the latitude and longitude of the vehicle
# @returns: [String] returns a string containing the delegation of the vehicle
def get_location(coords):
    
    try:
        # Calling the API
        geocoder_api = os.environ['GEOCODER_API']
        api_key = os.environ['GEOCODER_API_KEY']
        response = requests.get(f'{geocoder_api}latlng={coords}&result_type=route&key={api_key}').json()
        # Getting the specific address of the vehicle
        address = response['results'][0]['formatted_address'].split(', ')
        delegation = address[len(address) -4].lower()
        return delegation

    except:
        return 'Not available'