import json
import pickle
import numpy as np
"""from numpy.lib import utils
import pandas as pd"""

__locations = None
__data_columns = None
__model = None

file_path = "./artifacts/"
#file_path = "/home/main/Documents/IMSP/ML/Projects/prices prediction/codes/flask-server/server/artifacts/"
def get_estimated_price(location, sqft, bhk, bath):
    
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    print("location... : ")
    return  __locations


def load_save_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns
    global __locations
    global __model

    with open(file_path + "columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

        __locations = __data_columns[3:]

        #print(__data_columns)
    
    with open(file_path + "banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...done")

if __name__ == "__main__":
    load_save_artifacts()
    get_location_names()
    print(get_location_names())
    #print(__locations)

    ####### Some predictions#####
    print(get_estimated_price('1st phase jp nagar', 1000,3,3))
    print(get_estimated_price('1st phase jp nagar', 1000,2,2))
    """print(get_estimated_price('Kalhalli', 1000,2,2)) #other location
    print(get_estimated_price('Ejipura', 1000,2,2)) #other location"""
