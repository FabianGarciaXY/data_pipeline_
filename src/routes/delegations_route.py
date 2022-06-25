# Importing  Blueprint to use routes and jsonify and request for JSON responses
from flask import Blueprint, jsonify

# Blueprint for delegations routes
main = Blueprint('delegations_bp', __name__, url_prefix='/api/')


# Get a list of delegations
@main.route('/delegations', methods=['GET'])
def get_available_delegations():
    return jsonify({'message': 'This route will contain all delegations available'})

# Get vehicles in a given delegation
@main.route('/delegations/<string:name>', methods=['GET'])
def get_vehicles_by_delegation(name):
    return jsonify({'message': 'This route will contain all vehicles into a delegation', 'name': name})