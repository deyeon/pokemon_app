import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_data_app():
    df=pd.read_csv('data/pokedex_(Update_05.20).csv')
    df.set_index('pokedex_number',inplace=True)
    df=df.drop(df.columns[0],axis=1)
    df=df.dropna(axis=1)
    
    st.subheader('데이터 요약')
    st.dataframe(df.describe())

    st.subheader('포켓몬 별 최대/최소 데이터 확인하기')
    column_list = df.columns[8:]

    selected_column=st.selectbox('컬럼을 선택하세요',column_list)

    df_max=df.loc[df[selected_column]==df[selected_column].max(),]
    df_min=df.loc[df[selected_column]==df[selected_column].min(),]

    st.text('최대 데이터')
    st.dataframe(df_max)
    st.text('최소 데이터')
    st.dataframe(df_min)
    

    

