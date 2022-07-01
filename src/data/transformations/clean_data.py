from unidecode import unidecode
from data.transformations.dataframe import create_dataframe
from data.resources.inputs.reader import fetch_vehicles_data, get_location

# @description: Function to clear data and remove missing values
# @params: {function, function, function}, Functions to create the dataframe and get data and their location
# @returns: an updated dataframe
def clean_dataframe(dataframe, data, location):
    df = dataframe(data, location)
    # Removing missed and null values
    updated_df = df.fillna(0)
    # To lower case
    updated_df['delegation'] = df['delegation'].str.lower()
    # Removing accents
    updated_df['delegation'] = df['delegation'].apply(unidecode)
    return updated_df

# Calling the clean_dataframe function
df = clean_dataframe(create_dataframe, fetch_vehicles_data, get_location)