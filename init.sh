#!/bin/bash

# Get Data from api and load it into the database
echo "Getting data ..."
python ./src/utils/seed.py

echo "Done!"

# Run the server
python ./src/app.py