import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    
    x = np.zeros(244)  
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    try:
        
        loc_index = __data_columns.index(location.lower())
    
        if loc_index < 244:
            x[loc_index] = 1
    except:
        pass

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    
    json_path = r"C:\Users\pc\OneDrive\سطح المكتب\Project Machine_Learning\columns.json"
    pickle_path = r"C:\Users\pc\OneDrive\سطح المكتب\Project Machine_Learning\banglore_home_prices_model.pickle"
    global __model
    
    with open(json_path, "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open(pickle_path, "rb") as f:
        __model = pickle.load(f)
        
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) 
    print(get_estimated_price('Ejipura', 1000, 2, 2))  