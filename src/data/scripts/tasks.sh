#!/bin/bash

# Create vehicles table in aws postgres database
echo "Creating vehicles table"
# python ./src/api/models/vehicles.py

# Getting and cleaning data from api
echo "Getting data"
# python ./src/data/transformations/clean_data.py

# Saving data in database
echo "Saving data"
# python ./src/data/jobs/save_data.py

echo "Done!"

# Run the server
python ./src/api/app.py