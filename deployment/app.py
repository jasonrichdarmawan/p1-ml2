import streamlit as st
import frontend
import backend

navigation = st.sidebar.selectbox(label='Pilih Halaman', options=('EDA', 'Prediction'))

if navigation == 'EDA':
    pass
else:
    backend.run()