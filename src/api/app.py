from flask import Flask # This is the main module where the server starts
from routes import delegations, vehicles # Routes


# The app is created
app = Flask(__name__)

# Function to handle bad requests
def not_found(error):
    return '<h1>Page not found</h1>', 404


if __name__ == '__main__':
    # Blueprints for vehicles and delegations routes
    app.register_blueprint(vehicles.vehicle)
    app.register_blueprint(delegations.delegation)
    # Error handler
    app.register_error_handler(404, not_found)
    # Excuting the app
    app.run(debug=True, host='0.0.0.0', port=5000)