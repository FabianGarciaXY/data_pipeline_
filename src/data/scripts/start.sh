#!/bin/bash

# Get Data from api and load it into the database
echo "Creating vehicles table"
python ./src/api/models/vehicles.py

echo "Getting data ..."
python ./src/data/jobs/save_data.py
echo "Done!"

# Run the server
python ./src/api/app.py