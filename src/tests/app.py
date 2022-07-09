from api.app import app


# Function sample to validate tests are running correctly
def sum_values(value):
    return value + value

# The function test sample function
def test_function():
    assert sum_values(5) == 10
    

# Function to test flask app
def test_root_rout(): 
    flask_app = app.run()
    
    with flask_app.test_client() as client:
        response = client.get('/api')          
        assert response.status_code == 404