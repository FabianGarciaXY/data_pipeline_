import requests
import os

# Fething vehicle data from the API
def fetch_vehicles_data():

    try:
        url = os.environ['VEHICLES_API']
    except: 
        url = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=1000'

    response = requests.get(url)
    return response.json()