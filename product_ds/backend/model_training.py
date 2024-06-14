# %%
import pandas as pd
import numpy as np
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, LabelEncoder, OneHotEncoder
from sklearn.metrics import r2_score
import pickle
import joblib

# adding more features
def generatePolynomials(X):
    poly = PolynomialFeatures(degree=2)
    polyX = poly.fit_transform(X)
    return polyX

def train_housing():
    data = pd.read_csv('data/housing Train.csv')
    data.dropna(inplace=True)

    # # RESCALING
    scaler = StandardScaler()
    scaler.fit(data[[column for column in data.columns if column!='Median_House_Price']])
    with open('data/housing_scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f, protocol=4)
    data[[column for column in data.columns if column!='Median_House_Price']] = scaler.transform(data[[column for column in data.columns if column!='Median_House_Price']])

    # splitting into x, y
    X = data[[column for column in data.columns if column!='Median_House_Price']]
    y = data['Median_House_Price']

    X = generatePolynomials(X)

    # split into train, test
    validation_size = 0.2
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=validation_size, random_state=0) #stratify=X[['Charles_River_dummy_variable_(1_if_tract_bounds_river;_0_otherwise)']])

    # trainig model
    model = XGBRegressor(n_estimators=100, learning_rate=0.09
                        )
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_train)
    with open('data/housing_model.pkl', 'wb') as f:
        pickle.dump(model, f, protocol=4)
    
    print('Train metrics...')
    print('RMSE ', np.sqrt(mean_squared_error(y_train, y_pred)))
    print('r2_score: ', round(r2_score(y_train, y_pred)*100, 2))

    y_pred = model.predict(X_test)

    print('Validation metrics...')
    # rmse on actual scaled values
    print('RMSE ', np.sqrt(mean_squared_error(y_test, y_pred)))
    print('r2_score: ', round(r2_score(y_test, y_pred)*100, 2))

    y_pred = model.predict(X)
    
    return {'RMSE':round(np.sqrt(mean_squared_error(y, y_pred)), 2), 'r2_score':round(r2_score(y, y_pred)*100, 2)}

# train_housing()

def train_big_mart():
    data = pd.read_csv('data/Big Mart Sales Train.csv')
    # data.dropna(inplace=True)
    # data = data.reset_index(drop=True)

    data['Item_Weight'].fillna((data['Item_Weight'].mean()), inplace=True)
    data['Outlet_Size'].fillna('Small', inplace=True)

    ### reducing fat content to only two categories 
    data['Item_Fat_Content'] = data['Item_Fat_Content'].replace(['low fat','LF'], ['Low Fat','Low Fat']) 
    data['Item_Fat_Content'] = data['Item_Fat_Content'].replace(['reg'], ['Regular']) 

    # data['Item_Visibility'] = np.sqrt(data['Item_Visibility'])

    # splitting into x, y
    X = data[[column for column in data.columns if column not in ['Item_Outlet_Sales', 
                                                                'Outlet_Identifier', 
                                                                    'Item_Identifier']]]

    # X = pd.concat([X, pd.DataFrame.from_dict([{
    #     "Item_Weight": 12.85,
    #     "Item_Visibility": 0.06,
    #     "Item_Fat_Content": "Low Fat",
    #     "Item_Type": "Seafood",
    #     "Item_MRP": 140.99,
    #     "Outlet_Establishment_Year": 1997,
    #     "Outlet_Size": "High",
    #     "Outlet_Location_Type": "Tier 2",
    #     "Outlet_Type": "Grocery Store"
    #         }])])

    # X = X.reset_index(drop=True)

    y = data['Item_Outlet_Sales']
    # y = pd.concat([y, pd.Series([342])]).reset_index(drop=True)

    for i, feature in enumerate(['Outlet_Type', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type', 'Item_Fat_Content']):
        le = LabelEncoder()
        ohe = OneHotEncoder(sparse=False)

        # perform label encoding
        le.fit(X[feature])
        # save the encoder
        joblib.dump(le, open("data/le_{}.sav".format(feature), 'wb'))
        
        # transfrom training data
        X[feature] = le.transform(X[feature])

        # get classes & remove first column to elude from dummy variable trap
        columns = list(map(lambda x: feature+' '+str(x), list(le.classes_)))[1:]
        
        # save classes
        joblib.dump(columns, 
                    open("data/le_{}_classes.sav".format(feature), 'wb'))
        # load classes
        columns = joblib.load(
            open("data/le_{}_classes.sav".format(feature), 'rb'))

        
        if len(le.classes_)>2:
            # perform one hot encoding
            ohe.fit(X[[feature]])
            # save the encoder
            joblib.dump(ohe, open("data/ohe_{}.sav".format(feature), 'wb'))

            # transfrom training data
            # removing first column of encoded data to elude from dummy variable trap
            tempData = ohe.transform(X[[feature]])[:, 1:]

            # create Dataframe with columns as classes
            tempData = pd.DataFrame(tempData, columns=columns)
        else:
            tempData = X[[feature]]
        
        # create dataframe with all the label encoded categorical features along with hot encoding
        if i==0:
            encodedData = pd.DataFrame(data=tempData, columns=tempData.columns.values.tolist())
        else:
            encodedData = pd.concat([encodedData, tempData], axis=1)
        

    X = X[['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Outlet_Establishment_Year']]
    X = pd.concat([X, encodedData], axis=1)

    # # RESCALING
    scaler = StandardScaler()
    scaler.fit(X)
    with open('data/big_mart_scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f, protocol=4)
    X = scaler.transform(X)

    # adding more features
    # X = generatePolynomials(X)

    # split into train, test
    validation_size = 0.20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=validation_size, random_state=0)

    # trainig model
    # model = LinearRegression()
    model = XGBRegressor(
                        learning_rate=0.2,
                        n_estimators=100,
                        max_depth=10,
                        # min_child_weight=1,
                        # gamma=0.1,
                        alpha=0.8,
                        # reg_lambda=2,
                        # subsample=0.8,
                        # colsample_bytree=0.8,
                        eval_metric='rmse',
                        seed=7)

    model = model.fit(X_train, y_train)

    with open('data/big_mart_model.pkl', 'wb') as f:
        pickle.dump(model, f, protocol=4)

    y_pred = model.predict(X_train)

    print('Train metrics...')
    print('RMSE ', np.sqrt(mean_squared_error(y_train, y_pred)))
    print('r2_score: ', round(r2_score(y_train, y_pred)*100, 2))

    y_pred = model.predict(X_test)

    print('Validation metrics...')
    # rmse on actual scaled values
    print('RMSE ', np.sqrt(mean_squared_error(y_test, y_pred)))
    print('r2_score: ', round(r2_score(y_test, y_pred)*100, 2))

    y_pred = model.predict(X)

    return {'RMSE':round(np.sqrt(mean_squared_error(y, y_pred)), 2), 'r2_score':round(r2_score(y, y_pred)*100, 2)}

# train_big_mart()
