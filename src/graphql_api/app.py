from flask import Flask, request, jsonify
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from graphql_api.schema.schema import schema


# The app is created
app = Flask(__name__)


# Function to handle bad requests
def not_found(error):
    return '<h1>Page not found</h1>', 404

# GraphiQL playground is created
@app.route("/graphql/api", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

# GraphQL endpoint is created
@app.route("/graphql/api", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()
    # Flask, the current request will always be accessible as flask.request
    success, result = graphql_sync(schema, data, context_value=request,)
    status_code = 200 if success else 400
    
    return jsonify(result), status_code


if __name__ == '__main__':    
    # Error handler
    app.register_error_handler(404, not_found)
    # Excuting the app
    app.run(host='0.0.0.0', port=5000)