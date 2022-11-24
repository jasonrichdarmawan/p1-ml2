import streamlit as st
import joblib
import json
import pandas as pd

# Load Model
def isolate():
    global rf_pipe_tuned, rf_pipe_tuned_thr

    with open('./rf_pipe_tuned.pkl', 'rb') as file_1:
        rf_pipe_tuned = joblib.load(file_1)
    
    with open('./rf_pipe_tuned_threshold.txt', 'rt') as file_2:
        rf_pipe_tuned_thr = json.load(file_2)

isolate()

def run():
    with st.form(key='form_parameters'):
        Dependent_count = st.number_input(
            # min=0, max=5 (from data set)
            label='Number of dependents', 
            min_value=0
        )
        Months_on_book = st.number_input(
            # min=13, max_value=56
            label='Period of relationship with bank', 
            min_value=0
        )
        Total_Relationship_Count = st.number_input(
            # min=1, max=6
            label='Total no. of products held by the customer', 
            min_value=1, max_value=10
        )
        Contacts_Count_12_mon = st.number_input(
            # min=0, max=6
            label='No. of Contacts in the last 12 months', 
            min_value=0, max_value=12
        )
        Total_Revolving_Bal = st.number_input(
            # min=0, max=2517
            label='Total Revolving Balance on the Credit Card', 
            min_value=0
        )
        Total_Trans_Ct = st.number_input(
            # min=10, max=139
            label='Total Transaction Count (Last 12 months)',
            min_value=0,
        )
        Credit_Limit = st.number_input(
            # min=1,438.30, max=34,516.00
            label='Credit Limit on the Credit Card',
            min_value=0.,
        )
        Months_Inactive_12_mon = st.number_input(
            # min=0, max=6
            label='No. of months inactive in the last 12 months',
            min_value=0
        )
        Total_Amt_Chng_Q4_Q1 = st.number_input(
            # min=0.00, max=3.40
            label='Change in Transaction Amount (Q4 over Q1)',
            min_value=0.,
            max_value=4.
        )
        Total_Ct_Chng_Q4_Q1 = st.number_input(
            # min=0.00, max=3.71
            label='Change in Transaction Count (Q4 over Q1)',
            min_value=0.,
            max_value=4.
        )
        Education_Level = st.selectbox(
            # most frequent = 4
            label='Educational Qualification of the account holder',
            options=[
                'Unknown', 'Uneducated', 'High School', 'College', 'Graduate',
                'Post-Graduate', 'Doctorate'
            ],
            index=0
        )
        Gender = st.selectbox(
            # most frequent = Female
            label='Gender',
            options=['F', 'M'],
            index=0
        )
        Marital_Status = st.selectbox(
            # most frequent = Married
            label='Marital Status',
            options=['Unknown', 'Single', 'Married', 'Divorced'],
            index=2
        )
        Card_Category = st.selectbox(
            # most frequent = Blue
            label='Type of Card',
            options=['Blue', 'Silver', 'Gold', 'Platinum'],
            index=0
        )

        submitted = st.form_submit_button('Predict')

    inf_set = {
        'Dependent_count': Dependent_count,
        'Months_on_book': Months_on_book,
        'Total_Relationship_Count': Total_Relationship_Count,
        'Contacts_Count_12_mon': Contacts_Count_12_mon,
        'Total_Revolving_Bal': Total_Revolving_Bal,
        'Total_Trans_Ct': Total_Trans_Ct,
        'Credit_Limit': Credit_Limit,
        'Months_Inactive_12_mon': Months_Inactive_12_mon,
        'Total_Amt_Chng_Q4_Q1': Total_Amt_Chng_Q4_Q1,
        'Total_Ct_Chng_Q4_Q1': Total_Ct_Chng_Q4_Q1,
        'Education_Level': Education_Level,
        'Gender': Gender,
        'Marital_Status': Marital_Status,
        'Card_Category': Card_Category
    }

    if submitted:
        inf_set = pd.DataFrame([inf_set])

        y_inf_proba = rf_pipe_tuned.predict_proba(X=inf_set)[0,0]

        y_inf_proba_pred = (y_inf_proba <= rf_pipe_tuned_thr).astype(int)

        st.write('Prediction :', 
            pd.Series(y_inf_proba_pred)
              .map({0: 'Attrited Customer', 1: 'Existing Customer'})[0])