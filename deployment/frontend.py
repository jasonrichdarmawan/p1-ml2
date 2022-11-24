import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image

import frontend_nominal
import frontend_log

st.set_page_config(
    page_title='Internet Banking - PredictionBCA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    st.title('BCA Credit Card Attrition Flag Prediction')

    st.subheader('Exploratory Data Analysis of Credit Card Customer')

    st.write("Page ini dibuat oleh *Jason Rich Darmawan Onggo Putra*")

    target = 'Attrition_Flag'

    df = pd.read_csv('./BankChurners.csv')
    st.dataframe(df)

    st.write("## 4.1 - Log Transforma and Square Root Transform")
    
    st.write("Original")
    st.dataframe(frontend_log.agg_original_skew(df))
    
    st.write("Log Transform")
    st.dataframe(frontend_log.agg_log_skew(df))

    st.write("Square Root Transform")
    st.dataframe(frontend_log.agg_sqrt_skew(df))

    st.pyplot(frontend_log.plot_original_log(df))

    st.write("### 4.2.1 - X nominal features")
    st.pyplot(frontend_nominal.plot_nominal_features(df, target))

    st.write("### 4.2.2 - X numerical features")
    image = Image.open("./pairplot.png")
    st.image(image, caption='X numerical features')





