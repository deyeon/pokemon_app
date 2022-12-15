import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app():
    df=pd.read_csv('data/pokedex_(Update_05.20).csv')
    df.set_index('pokedex_number',inplace=True)
    df=df.drop(df.columns[0],axis=1)
    df=df.dropna(axis=1)
    
    st.subheader('통계 데이터 확인')
    st.dataframe(df.head(3))
    
    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    st.subheader('최대/최소 데이터 확인하기')
    column_list = df.columns[8:]

    selected_column=st.selectbox('컬럼을 선택하세요',column_list)

    df_max=df.loc[df[selected_column]==df[selected_column].max(),]
    df_min=df.loc[df[selected_column]==df[selected_column].min(),]

    st.text('최대 데이터')
    st.dataframe(df_max)
    st.text('최소 데이터')
    st.dataframe(df_min)

    st.subheader('컬럼 별 히스토그램')

    df2=df.loc[:,['generation','status','type_1']]

    column_list2 = df2.columns
    histogram_coulmn=st.selectbox('히스토그램 확인 할 컬럼을 선택하세요',column_list2)

    import plotly.express as px

    fig=px.histogram(df2,x=histogram_coulmn,nbins=20)
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig)

    st.subheader('파이 차트')
    fig1 = px.pie(df2,names=df2[histogram_coulmn].value_counts().index,values=df2[histogram_coulmn].value_counts(),title='파이차트')
    st.plotly_chart(fig1)

    

