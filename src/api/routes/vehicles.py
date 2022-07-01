# Importing  Blueprint to use routes and jsonify and request for JSON responses
from flask import Blueprint, jsonify
import api.controllers.vehicles as controller

# Blueprint for vehicles routes
vehicle = Blueprint('vehicles_bp', __name__, url_prefix='/api/')


# root route `/api/`
@vehicle.route('/')
def root():
    return jsonify({'message': 'Hi World!'})


# Get all available vehicles
@vehicle.route('/metrobuses', methods=['GET'])
def get_available_vehicles():
    vehicles = controller.get_available_vehicles()
    return jsonify(vehicles)


# Get vehicle location by ID
@vehicle.route('/metrobuses/<int:id>', methods=['GET'])
def get_vehicle_address_by_id(id):
    vehicle = controller.get_vehicle_address_by_id(id)
    return jsonify({'vehicle': vehicle})