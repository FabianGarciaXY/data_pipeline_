#!/bin/bash

# Get Data from api and load it into the database
python ./src/utils/seed.py

# Run the server
python ./src/app.py