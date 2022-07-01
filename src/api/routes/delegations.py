# Importing  Blueprint to use routes and jsonify and request for JSON responses
from flask import Blueprint, jsonify
import api.controllers.delegations as controller

# Blueprint for delegations routes
delegation = Blueprint('delegations_bp', __name__, url_prefix='/api/')

# Get a list of delegations
@delegation.route('/delegations', methods=['GET'])
def get_available_delegations():
    delegations = controller.get_available_delegations()
    return jsonify({'alcaldias': delegations})


# Get vehicles in a given delegation
@delegation.route('/delegations/<string:name>', methods=['GET'])
def get_vehicles_by_delegation(name):
    vehicles = controller.get_vehicles_by_delegation(name)
    return jsonify(vehicles)