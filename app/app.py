from flask import Flask # This is the main module where the server starts
from routes import vehicles_route, delegations_route # Routes


# The app is created
app = Flask(__name__)

# Function to handle bad requests
def not_found(error):
    return '<h1>Page not found</h1>', 404


if __name__ == '__main__':

    # Blueprints for vehicles
    app.register_blueprint(vehicles_route.main)

    # Blueprints for delegations
    app.register_blueprint(delegations_route.main)

    # Error handler
    app.register_error_handler(404, not_found)
    app.run(host='0.0.0.0', port=5000)