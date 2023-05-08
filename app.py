import streamlit as st
import pandas as pd
import numpy as np

ocean_filename = 'data/2023-05-08 13:56:03.971866_laisuat_oceanbank.csv'
vietin_filename = 'data/2023-05-08 09:00:04.857170_laisuat_vietinbank.csv'
agri_filename = 'data/2023-05-08 13:31:39.015117_laisuat_agribank_cn.csv'

st.set_page_config(layout="wide") 
st.header('Theo dõi lãi suất huy động các ngân hàng thương mại')

col1, col2 = st.columns(2)

with col1:
    st.header("1st bank")
    option1 = st.selectbox(
        'Chọn ngân hàng',
        ('Vietin Bank', 'Agribank', 'Ocean Bank'), key='bank1')
    if option1 == 'Vietin Bank':
        df = pd.read_csv(vietin_filename)
    elif option1 == 'Agribank':
        df = pd.read_csv(agri_filename)
    else:
        df = pd.read_csv(ocean_filename)
    st.table(df)

with col2:
    st.header("2nd bank")
    option2 = st.selectbox(
        'Chọn ngân hàng',
        ('Vietin Bank', 'Agribank', 'Ocean Bank'), key='bank2')
    if option2 == 'Vietin Bank':
        df2 = pd.read_csv(vietin_filename)
    elif option2 == 'Agribank':
        df2 = pd.read_csv(agri_filename)
    else:
        df2 = pd.read_csv(ocean_filename)
    st.table(df2)

