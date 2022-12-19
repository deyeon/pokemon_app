import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_chart_app():
    df=pd.read_csv('data/pokedex_(Update_05.20).csv')
    df.set_index('pokedex_number',inplace=True)
    df=df.drop(df.columns[0],axis=1)
    df=df.dropna(axis=1)

    st.subheader('컬럼 별 히스토그램')

    df2=df.loc[:,['generation','status','type_1']]

    column_list2 = df2.columns
    status1 =st.radio('설정을 선택하세요',['세대별','등급별','타입별'])

    import plotly.express as px
    if status1 == '세대별' :
        st.header('세대별 히스토그램')
        fig1=px.histogram(df2,x=df2['generation'],nbins=20,color_discrete_sequence=["green"])
        fig1.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig1)
        
        st.subheader('파이 차트')
        fig2 = px.pie(df2,names=df2['generation'].value_counts().index,values=df2['generation'].value_counts(),title='파이차트')
        st.plotly_chart(fig2)
    
    elif status1 == '등급별' :
        st.header('등급별 히스토그램')
        fig3=px.histogram(df2,x=df2['status'],nbins=20,color_discrete_sequence=['blue'])
        fig3.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig3)
        
        st.subheader('파이 차트')
        fig4 = px.pie(df2,names=df2['status'].value_counts().index,values=df2['status'].value_counts(),title='파이차트')
        st.plotly_chart(fig4)

    elif status1 == '타입별' :
        st.header('타입별 히스토그램')
        fig5=px.histogram(df2,x=df2['type_1'],nbins=20,color_discrete_sequence=['red'])
        fig5.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig5)
        
        st.subheader('파이 차트')
        fig6 = px.pie(df2,names=df2['type_1'].value_counts().index,values=df2['type_1'].value_counts(),title='파이차트')
        st.plotly_chart(fig6)

