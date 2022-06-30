import pandas as pd

# Module to transform json data into a dataframe using pandas library

# @description: Function to create a dataframe.
# @params: {function, function}, must receive a function to fetch data from vehicles and a another to get their locations.
# @return: a dataframe with the values.
def create_dataframe(fetch_data, get_location):
    data = fetch_data()
    vehicles_list = []

    for vehicle in data:
        # The get_location function, gives us the delegation of each vehicle        
        delegation = get_location(vehicle['geographic_point']); 
        print(delegation, sep='-')
        # 
        vehicles_list.append({
            'date_updated': vehicle['date_updated'], 
            'vehicle_id': vehicle['vehicle_id'], 
            'vehicle_label': vehicle['vehicle_label'], 
            'vehicle_current_status': vehicle['vehicle_current_status'], 
            'position_latitude': vehicle['position_latitude'],
            'position_longitude': vehicle['position_longitude'], 
            'geographic_point': vehicle['geographic_point'], 
            'position_speed': vehicle['position_speed'], 
            'position_odometer': vehicle['position_odometer'], 
            'trip_schedule_relationship': vehicle['trip_schedule_relationship'], 
            'trip_id': vehicle['trip_id'], 
            'trip_start_date': vehicle['trip_start_date'],
            'trip_route_id': vehicle['trip_route_id'],
            'delegation': delegation
        })
    return pd.DataFrame(vehicles_list)