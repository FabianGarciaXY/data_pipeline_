from flask import jsonify
from ariadne import QueryType
import graphql_api.services.vehicles as vehicle_service
import graphql_api.services.delegation as delegation_service


query = QueryType()


# Resolver to get all available vehicles
@query.field('get_vehicles')
def get_vehicles(*_):
    vehicles = vehicle_service.get_vehicles()
    return vehicles


# Resolver to get the position of a vehicle given its id
@query.field('get_vehicle_address_by_id')
def get_vehicle_address_by_id(obj, info, id):    
    vehicle = vehicle_service.get_vehicle(id)
    if vehicle: 
        return vehicle
    else:
        return {'message': 'vehicle with this id does not exist'}

# Resolver to get all available delegations
@query.field('get_delegations')
def get_delegations(obj, info): 
    return [{"name": "awdwad"}, {"name": "awdawd"}]


# Resolver to get vehicles into a delegation
@query.field('get_vehicles_by_delegation')
def get_vehicles_by_delegation(obj, info, name):
    return [
        {"id": 1, "vehicle_id": 1, "date_updated": "2020-01-01", "vehicle_label": 1, "vehicle_current_status": "active", "position_latitude": 1.0, "position_longitude": 1.0, "geographic_point": "1.0,1.0", "position_speed": 1, "position_odometer": 1, "trip_schedule_relationship": 1, "trip_id": 1, "trip_start_date": "2020-01-01", "trip_route_id": 1, "delegation": 1, "created_at": "2020-01-01"},
        {"id": 2, "vehicle_id": 2, "date_updated": "2020-01-01", "vehicle_label": 2, "vehicle_current_status": "active", "position_latitude": 2.0, "position_longitude": 2.0, "geographic_point": "2.0,2.0", "position_speed": 2, "position_odometer": 2, "trip_schedule_relationship": 2, "trip_id": 2, "trip_start_date": "2020-01-01", "trip_route_id": 2, "delegation": 2, "created_at": "2020-01-01"},
    ]