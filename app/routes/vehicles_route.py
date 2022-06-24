# Blueprint to use routes and jsonify for JSON responses
from flask import Blueprint, jsonify , request

# Blueprint for api
main = Blueprint('vehicles_blueprint', __name__, url_prefix='/api/')

# root route
@main.route('/')
def root():
    return jsonify({'message': 'Hi World!'})

# Get all available vehicles
@main.route('/metrobuses')
def metrobuses():
    return jsonify({'message': 'This page will contain info about vehicles'})

# Get vehicle location by ID
@main.route('/metrobuses/<int:id>')
def get_metrobuses_by_id(id):
    return jsonify({'message': id})