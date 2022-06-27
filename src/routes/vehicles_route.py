# Importing  Blueprint to use routes and jsonify and request for JSON responses
from crypt import methods
from flask import Blueprint, jsonify , request

# Blueprint for vehicles routes
main = Blueprint('vehicles_bp', __name__, url_prefix='/api/')


# root route `/api/`
@main.route('/')
def root():
    return jsonify({'message': 'Hi World!'})

# Get all available vehicles
@main.route('/metrobuses', methods=['GET'])
def get_available_vehicles():
    return jsonify({'message': 'This page will contain info about vehicles'})

# Get vehicle location by ID
@main.route('/metrobuses/<int:id>', methods=['GET'])
def get_vehicle_addres_by_id(id):
    return jsonify({'message': id})