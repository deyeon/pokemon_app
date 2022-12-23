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
    st.text('각 기준을 선택하시면 그 기준별로 히스토그램과 파이차트를 보실수 있습니다.')
    df2=df.loc[:,['generation','status','type_1']]

    column_list2 = df2.columns
    status1 =st.radio('설정을 선택하세요',['세대별','등급별','타입별'])
    st.text("각 기준별로 데이터가 얼마나 분포되어 있는지 나타낸 히스토그램입니다.")

    import plotly.express as px
    if status1 == '세대별' :
        
        st.header('세대별 히스토그램')
        st.text("세대별로 데이터가 얼마나 분포되어 있는지 나타낸 히스토그램입니다.")
        fig1=px.histogram(df2,x=df2['generation'],nbins=20,color_discrete_sequence=["green"])
        fig1.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig1)
        
        st.subheader('파이 차트')
        st.text("세대별로 데이터가 얼마나 점유율을 차지하는지 나타낸 파이차트입니다.")
        fig2 = px.pie(df2,names=df2['generation'].value_counts().index,values=df2['generation'].value_counts(),title='파이차트')
        st.plotly_chart(fig2)
    
    elif status1 == '등급별' :
        st.header('등급별 히스토그램')
        st.text("등급별로 데이터가 얼마나 분포되어 있는지 나타낸 히스토그램입니다.")
        fig3=px.histogram(df2,x=df2['status'],nbins=20,color_discrete_sequence=['blue'])
        fig3.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig3)
        
        st.subheader('파이 차트')
        st.text("등급별로 데이터가 얼마나 점유율을 차지하는지 나타낸 파이차트입니다.")
        fig4 = px.pie(df2,names=df2['status'].value_counts().index,values=df2['status'].value_counts(),title='파이차트')
        st.plotly_chart(fig4)

    elif status1 == '타입별' :
        st.header('타입별 히스토그램')
        st.text("타입별로 데이터가 얼마나 분포되어 있는지 나타낸 히스토그램입니다.")
        fig5=px.histogram(df2,x=df2['type_1'],nbins=20,color_discrete_sequence=['red'])
        fig5.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig5)
        
        st.subheader('파이 차트')
        st.text("등급별로 데이터가 얼마나 점유율을 차지하는지 나타낸 파이차트입니다.")
        fig6 = px.pie(df2,names=df2['type_1'].value_counts().index,values=df2['type_1'].value_counts(),title='파이차트')
        st.plotly_chart(fig6)

    st.subheader('상관관계 분석')
    st.text("각 컬럼간의 상관관계를 분석하였습니다.")
    st.text("컬럼을 선택하여 상관분석을 할수 있습니다.")
    
    c_list = df.columns[5:]
    selected_list=st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', c_list)

    if len(selected_list) >= 2:
            df_corr=df[selected_list].corr()
            fig7 = plt.figure()
            sb.heatmap(data=df_corr,annot=True,fmt='.2f',cmap='coolwarm',
            vmin = -1,vmax=1,linewidths=0.5)
            st.pyplot(fig7)



