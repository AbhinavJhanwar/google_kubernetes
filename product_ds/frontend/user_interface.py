# streamlit run user_interface.py --server.fileWatcherType none
# stremalit run user_interface.py --server.port 8085
import streamlit as st
import requests

def train_data(dataset_name):
    url = "http://fastapi:8000/train"
    # url = "http://0.0.0.0:8000/train"

    response = requests.post(url, json={"dataset_name":dataset_name})
    return eval(response.text)

def predict_data(dataset_name, data):
    url = "http://fastapi:8000/predict"
    # url = "http://0.0.0.0:8000/predict"

    response = requests.post(url, json={"dataset_name":dataset_name, "sample":data})
    return eval(response.text)

st.title("Data Science Use Case Demo")

dataset = st.radio("Select Dataset-", options=["House Price", "Big Mart Sales"])#on_change
data = {}
if dataset=='House Price':
    train_metric = train_data(dataset)
    col1, col2 = st.columns(2)
    col1.metric("RMSE", train_metric['summary']['RMSE'])
    col2.metric("R2 Score", train_metric['summary']['r2_score'])
    
    per_capita_crime_rate = st.slider('Per Capita Crime Rate', min_value=0.06, max_value=90.0, value=3.61)#on_change
    proportion_of_residential_land_over_25000_sq = st.slider('Proportion of residential land over 25000 square foot', min_value=0.0, max_value=100.0, value=11.43)#on_change
    proportion_of_non = st.slider('Proportion of Non-Retail Business Acres Per Town', min_value=0.46, max_value=28.0, value=11.1)#on_change
    Charles_River_dummy_variable = st.radio('Charles River Tract Bound', options=[0, 1], horizontal=True)#on_change
    nitric_oxides_concentration = st.slider('Nitric Oxides Concentration (parts per 10 million)', min_value=0.3, max_value=0.9, value=0.55)#on_change
    average_number_of_rooms_per_dwelling = st.slider('Average Number of Rooms Per Dwelling', min_value=3.5, max_value=9.0, value=6.28)#on_change
    proportion_of_owner = st.slider('Proportion of Owner Occupied Units Built Prior to 1940', min_value=2.9, max_value=100.0, value=68.64)#on_change
    weighted_distances_to_five_Boston_employment_centres = st.slider('Weighted Distances to Five Boston Employment Centres', min_value=1.0, max_value=13.0, value=3.79)#on_change
    index_of_accessibility_to_radial_highways = st.slider('Index of Accessibility to Radial Highways', min_value=1.0, max_value=24.0, value=9.53)#on_change
    full = st.slider('Full Value Property Tax Rate per $10000', min_value=187.0, max_value=711.0, value=407.72)#on_change
    pupil = st.slider('Pupil Teacher Ratio By Town', min_value=12.0, max_value=22.0, value=18.45)#on_change

    data = {'per_capita_crime_rate':per_capita_crime_rate,
            'proportion_of_residential_land_over_25000_sq.ft.':proportion_of_residential_land_over_25000_sq,
            'proportion_of_non-retail_business_acres_per_town':proportion_of_non,
            'Charles_River_dummy_variable_(1_if_tract_bounds_river;_0_otherwise)':Charles_River_dummy_variable,
            'nitric_oxides_concentration_(parts_per_10_million)':nitric_oxides_concentration,
            'average_number_of_rooms_per_dwelling':average_number_of_rooms_per_dwelling,
            'proportion_of_owner-occupied_units_built_prior_to_1940':proportion_of_owner,
            'weighted_distances_to_five_Boston_employment_centres':weighted_distances_to_five_Boston_employment_centres,
            'index_of_accessibility_to_radial_highways':index_of_accessibility_to_radial_highways,
            'full-value_property-tax_rate_per_$10000':full,
            'pupil-teacher_ratio_by_town':pupil}

    if st.button('Predict Median House Price'):
        prediction = round(float(predict_data(dataset_name=dataset, data=data)["summary"]["prediction"]), 2)
        st.caption(f"Median :house_with_garden: Price: :heavy_dollar_sign: :blue[{prediction}]")
        st.snow()
    
elif dataset=='Big Mart Sales':
    train_metric = train_data(dataset)
    col1, col2 = st.columns(2)
    col1.metric("RMSE", train_metric['summary']['RMSE'])
    col2.metric("R2 Score", train_metric['summary']['r2_score'])
    
    Item_Weight = st.slider('Item Weight', min_value=4.0, max_value=22.0, value=12.85)#on_change
    Item_Fat_Content = st.radio('Item Fat Content', ['Low Fat', 'Regular'], horizontal=True)
    Item_Visibility = st.slider('Item Visibility', min_value=0.0, max_value=0.4, value=0.06)#on_change
    Item_Type = st.selectbox('Item Type', ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables',
                                            'Household', 'Baking Goods', 'Snack Foods', 'Frozen Foods',
                                            'Breakfast', 'Health and Hygiene', 'Hard Drinks', 'Canned',
                                            'Breads', 'Starchy Foods', 'Seafood', 'Others'], index=3)
    Item_MRP = st.slider('Item MRP', min_value=31.0, max_value=267.0, value=140.99)#on_change
    Outlet_Establishment_Year = st.slider('Outlet Establishment year', min_value=1985, max_value=2009, value=1997)#on_change
    Outlet_Size = st.radio('Outlet Size', ['Small', 'Medium', 'High'], horizontal=True)
    Outlet_Location_Type = st.radio('Outlet Location Type', ['Tier 1', 'Tier 2', 'Tier 3'], horizontal=True)
    Outlet_Type = st.radio('Outlet Type', ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'], horizontal=True)

    data = {
        'Item_Weight':Item_Weight,
        'Item_Visibility':Item_Visibility,
        'Item_Fat_Content':Item_Fat_Content,
        'Item_Type':Item_Type,
        'Item_MRP':Item_MRP,
        'Outlet_Establishment_Year':Outlet_Establishment_Year,
        'Outlet_Size':Outlet_Size,
        'Outlet_Location_Type':Outlet_Location_Type,
        'Outlet_Type':Outlet_Type
    }
    
    if st.button('Predict Item Outlet Sales'):
        prediction = round(float(predict_data(dataset_name=dataset, data=data)["summary"]["prediction"]), 2)
        st.caption(f"Item Outlet Sales: :heavy_dollar_sign: :blue[{prediction}]")
        st.snow()

