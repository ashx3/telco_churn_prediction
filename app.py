import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

url = "https://raw.githubusercontent.com/ashx3/telco_churn_prediction/main/tel_churn.csv"
data = pd.read_csv(url)

# title and starters
st.title('Telecom Churn Prediction App')

st.write('---')

name = st.text_input('Enter your name:')

st.subheader(f'Hi {name},')

st.markdown(f'''The Telecom Churn Prediction App is used to detect whether a Customer will Churn or not Churn based on his behavior and features. 
            Here, the user has to select the relevant options below to generate results. The generated results are predicted by the 
            trained model with confidence levels, these predictions are made after training the model with the attributes and 
            characteristics of Churners & Non-Churners.''')

# inputs
gender = st.radio('Select your Gender:', ('Male', 'Female'))

senior_citizen = st.radio('Are you a Senior Citizen?', ('No', 'Yes'))

partner = st.radio('Do you have a partner?', ('Yes', 'No'))

dependents = st.radio('Do you have any dependents?', ('Yes', 'No'))

phone_service = st.radio('Do you use phone services?', ('Yes', 'No'))

multiple_lines = st.radio('Do you use multiple lines?', ('Yes', 'No'))

internet_service = st.radio('What mode do you use to access internet services?', ( 'DSL', 'Fiber optic','No'))

online_security = st.radio('Do you use online security?', ('Yes', 'No'))

online_backup = st.radio('Do you use online backup?', ('Yes', 'No'))

device_protection = st.radio('Do you use device protection?', ('Yes', 'No'))

tech_support = st.radio('Do you use tech support?', ('Yes', 'No'))

streaming_tv = st.radio('Do you use streaming services on TV?', ('Yes', 'No'))

streaming_movies = st.radio('Do you steam movies?', ('Yes', 'No'))

paperless_billing = st.radio('Do you use paperless billing?', ('Yes', 'No'))

contract = st.selectbox("What type of Contract Term are you subscribed?",
                         ['Month-to-month', 'One year', 'Two year'])
 
st.success(f"Contract Type - {contract}")

monthly_charges = st.slider('Monthly Charges (USD)', min(data['MonthlyCharges']), max(data["MonthlyCharges"]))

total_charges = st.slider('Total Charges (USD)', min(data['TotalCharges']), max(data["TotalCharges"]))

payment_method = st.selectbox("What type of payment method do you use :",
                         ['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)'])

tenure_group = st.selectbox("How many months have you been using the services?", 
                         ['1 - 12', '13 - 24', '25 - 36', '37 - 48', '61 - 72', '49 - 60'], help = 'Tenure')

# inputs and columns for prediction
input = [[gender, senior_citizen, partner, dependents, phone_service, multiple_lines, internet_service, online_security,
            online_backup, device_protection, tech_support, streaming_tv, streaming_movies, contract, paperless_billing, 
            payment_method, monthly_charges, total_charges, tenure_group]]

cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
       'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
       'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges',
       'TotalCharges', 'tenure_group']

# creating a dataframe for inputs
predictor = pd.DataFrame(input, columns=cols)

# func for encoding inputs and predicting the inputs
def preprocess_predictor(data):
    # loading encoders
    with open('StandardScaler', 'rb') as f:
        ss = pickle.load(f)

    with open('One-Hot-Encoder', 'rb') as f:
        ohe = pickle.load(f)

    # categorical columns
    cat_cols = [col for col in data.columns if data[col].dtype == 'object']

    # numerical columns
    num_cols = [col for col in data.columns if data[col].dtype != 'object']

    # standard scaler for predictor
    data[num_cols] = ss.transform(data[num_cols])

    # one-hot-encoding for predictor
    data_ohe = ohe.transform(data[cat_cols])

    col_ohe = ohe.get_feature_names(cat_cols)

    data_ohe_df = pd.DataFrame(data_ohe, columns = col_ohe, index = data.index)

    data_final = pd.concat([data.drop(columns=cat_cols), data_ohe_df], axis=1)

    with open('model.sav', 'rb') as f:
        model = pickle.load(f)

    single = model.predict(data_final)
    probability = model.predict_proba(data_final)

    if single == 1:
        st.error("The customer is likely to be Churn!!")
        st.warning("Confidence = {}".format(probability[:,1] * 100) + '%')
    else:
        st.success("The customer is likely to continue !!")
        st.warning("The Confidence level is about {}".format(*probability[:, 0] * 100) + '%')
        st.write('---')

if(st.button('Predict')):
    preprocess_predictor(predictor)

# remove main menu and footer note of streamlit
hide_menu_style = '''
       <style>
       #MainMenu {visibility: hidden;}
       footer{visibility: hidden;}
       </style>
        '''
st.markdown(hide_menu_style, unsafe_allow_html=True)