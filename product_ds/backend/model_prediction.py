# %% 
import pickle
import pandas as pd
from model_training import generatePolynomials
import joblib

def predict_big_mart(data):
    X_test = pd.DataFrame.from_dict([data])

    for i, feature in enumerate(['Outlet_Type', 'Outlet_Location_Type', 
                                'Outlet_Size', 'Item_Type',
                                'Item_Fat_Content']):
        
        
        # load the encoder
        le = joblib.load(open("data/le_{}.sav".format(feature), 'rb'))
        
        # transfrom training data
        X_test[feature] = le.transform(X_test[feature])
        
        # load classes
        columns = joblib.load(open("data/le_{}_classes.sav".format(feature), 'rb'))

        
        try:
            # load the encoder
            ohe = joblib.load(open("data/ohe_{}.sav".format(feature), 'rb'))

            # transfrom training data
            # removing first column of encoded data to elude from dummy variable trap
            tempData = ohe.transform(X_test[[feature]])[:, 1:]

            # create Dataframe with columns as classes
            tempData = pd.DataFrame(tempData, columns=columns)
        except:
            tempData = X_test[[feature]]
        
        # create dataframe with all the label encoded categorical features along with hot encoding
        if i==0:
            encodedData = pd.DataFrame(data=tempData, columns=tempData.columns.values.tolist())
        else:
            encodedData = pd.concat([encodedData, tempData], axis=1)
        

    X_test = X_test[['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Outlet_Establishment_Year']]
    X_test = pd.concat([X_test, encodedData], axis=1)

    # # RESCALING
    with open('data/big_mart_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    X_test = scaler.transform(X_test)

    # adding more features
    # X_test = generatePolynomials(X_test)

    with open('data/big_mart_model.pkl', 'rb') as f:
        model = pickle.load(f)

    y_test = list(model.predict(X_test))
    
    return {"prediction": str(y_test[0])}

def predict_housing(data):
    X_test = pd.DataFrame.from_dict([data])

    with open('data/housing_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    with open('data/housing_model.pkl', 'rb') as f:
        model = pickle.load(f)

    X_test = scaler.transform(X_test)
    X_test = generatePolynomials(X_test)
    y_test = list(model.predict(X_test))
    
    return {"prediction": str(y_test[0])}


# data = {"per_capita_crime_rate":0.00632,
#         "proportion_of_residential_land_over_25000_sq.ft.":18,
#         "proportion_of_non-retail_business_acres_per_town":2.31,
#         "Charles_River_dummy_variable_(1_if_tract_bounds_river;_0_otherwise)":0,
#         "nitric_oxides_concentration_(parts_per_10_million)":0.538,
#         "average_number_of_rooms_per_dwelling":6.575,
#         "proportion_of_owner-occupied_units_built_prior_to_1940":65.2,
#         "weighted_distances_to_five_Boston_employment_centres":4.09,
#         "index_of_accessibility_to_radial_highways":1,
#         "full-value_property-tax_rate_per_$10000":296,
#         "pupil-teacher_ratio_by_town":15.3}
# # 24

# predict_housing(data)