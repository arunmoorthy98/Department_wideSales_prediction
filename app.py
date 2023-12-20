import streamlit as st
import pickle
import pandas as pd

# Setting Webpage Configurations
st.set_page_config(page_icon="⚙",page_title="Sales Predictor", layout="wide")

st.title(':green[Forecast360] - Your Ultimate Sales Predictor 🚀')

@st.cache_resource
def load_model():
    model = pickle.load(open('Models\Predictor_model\model.pkl', 'rb'))
    return model

model = load_model()

transformer = pickle.load(open('Models\Transformer\model.pkl','rb'))

col1,col2 = st.columns(2)

col3,col4 = st.columns(2)

col5,col6 = st.columns(2)

col7,col8 = st.columns(2)

with col1:
    Year = st.selectbox('Select a Year', options = [2010, 2011, 2012])

with col2:
    store_range = list(range(1, 46))
    Store = st.selectbox('Select the store', options = store_range)

with col3:
    Store_Type = st.selectbox('Select the Type', options = ['A','B','C'])

with col4:
    dept_range = list(range(1, 100))
    Department = st.selectbox('Select the Department', options = dept_range)

with col5:
    Temperature = st.number_input('Enter the Temperature')

with col6:
    Fuel_Price = st.number_input('Enter the Fuel Price')

with col7:
    CPI =  st.number_input('Enter the CPI')

with col8:
    Unemployment = st.number_input('Enter the Unemployment Rate')

user_input = pd.DataFrame([[Year,Store,Store_Type,Department,Temperature,Fuel_Price,CPI,Unemployment]], columns = ['Year','Store','Store_Type','Dept','Temperature','Fuel_Price','CPI','Unemployment'])

submit = st.button('Predict Sales')

if submit:
    user_input_transformed = transformer.transform(user_input)
  
    result = model.predict(user_input_transformed)
    st.header(f':green[Predicted Sales] : {result}')