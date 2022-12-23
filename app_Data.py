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
    st.text("각 컬럼별로 최대/최소데이터를 확인 할수 있습니다.")
    column_list = ["종합","체력","공격","방어","특수공격","특수방어","속도"]

    selected_column=st.selectbox('컬럼을 선택하세요',column_list)

    if selected_column == "종합":
        df_max=df.loc[df['total_points']==df['total_points'].max(),]
        df_min=df.loc[df['total_points']==df['total_points'].min(),]

        st.text('종합 최대')
        st.text('무한다이노 거다이맥스폼')
        st.image("https://www.serebii.net/swordshield/pokemon/890-e.png")
        st.dataframe(df_max)
        st.text('종합 최소')
        st.text('약어리 평소모습')
        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/074601.png")
        st.dataframe(df_min)
    
    elif selected_column == "체력":
        df_max=df.loc[df['hp']==df['hp'].max(),]
        df_min=df.loc[df['hp']==df['hp'].min(),]

        st.text('체력 최대')
        st.text('해피너스,무한다이노 거다이맥스폼')
        col1,col2 = st.columns(2)
        col1.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/024201.png",use_column_width=True)
        col2.image("https://www.serebii.net/swordshield/pokemon/890-e.png",use_column_width=True)
        st.dataframe(df_max)
        st.text('체력 최소')
        st.text('껍질몬')
        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/029201.png")
        st.dataframe(df_min)
    
    elif selected_column == "공격":
        df_max=df.loc[df['attack']==df['attack'].max(),]
        df_min=df.loc[df['attack']==df['attack'].min(),]

        st.text('공격 최대')
        st.text('뮤츠 메가진화 X폼')
        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/015002.png")
        st.dataframe(df_max)
        st.text('공격 최소')
        st.text('럭키,핑복')
        col1,col2 = st.columns(2)
        col1.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/011301.png",use_column_width=True)
        col2.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/044001.png",use_column_width=True)
        st.dataframe(df_min)
    
    elif selected_column == "방어":
        df_max=df.loc[df['defense']==df['defense'].max(),]
        df_min=df.loc[df['defense']==df['defense'].min(),]

        st.text('방어 최대')
        st.text('무한다이노 거다이맥스폼')
        st.image("https://www.serebii.net/swordshield/pokemon/890-e.png")
        st.dataframe(df_max)
        st.text('방어 최소')
        st.text('럭키,핑복')
        col1,col2 = st.columns(2)
        col1.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/011301.png",use_column_width=True)
        col2.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/044001.png",use_column_width=True)
        st.dataframe(df_min)

    elif selected_column == "특수공격":
        df_max=df.loc[df['sp_attack']==df['sp_attack'].max(),]
        df_min=df.loc[df['sp_attack']==df['sp_attack'].min(),]

        st.text('특수공격 최대')
        st.text('뮤츠 메가진화 y폼')
        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/015003.png")
        st.dataframe(df_max)
        st.text('특수공격 최소')
        st.text('모래두지 알로라폼,단단지,빈티나,꼬지지')
        col1,col2,col3,col4 = st.columns(4)
        col1.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/002702.png",use_column_width=True)
        col2.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/021301.png",use_column_width=True)
        col3.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/034901.png",use_column_width=True)
        col4.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/043801.png",use_column_width=True)
        st.dataframe(df_min)

    elif selected_column == "특수방어":
        df_max=df.loc[df['sp_defense']==df['sp_defense'].max(),]
        df_min=df.loc[df['sp_defense']==df['sp_defense'].min(),]

        st.text('특수방어 최대')
        st.text('무한다이노 거다이맥스폼')
        st.image("https://www.serebii.net/swordshield/pokemon/890-e.png")
        st.dataframe(df_max)
        st.text('특수방어 최소')
        st.text('캐터피,뿔충이,잉어킹,푸푸린,샤프니아,테오키스 어택폼,돌헨진')
        col1,col2,col3,col4,col5,col6,col7=st.columns(7)
        col1.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/001001.png",use_column_width=True)
        col2.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/001301.png",use_column_width=True)
        col3.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/012901.png",use_column_width=True)
        col4.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/017401.png",use_column_width=True)
        col5.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/031801.png",use_column_width=True)
        col6.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/038602.png",use_column_width=True)
        col7.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/087401.png",use_column_width=True)
        st.dataframe(df_min)

    elif selected_column == "속도":
        df_max=df.loc[df['speed']==df['speed'].max(),]
        df_min=df.loc[df['speed']==df['speed'].min(),]

        st.text('속도 최대')
        st.text('테오키스 스피드폼')
        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/038604.png")
        st.dataframe(df_max)
        st.text('속도 최소')
        st.text('단단지,먹고자,해무기')
        col1,col2,col3=st.columns(3)
        col1.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/021301.png",use_column_width=True)
        col2.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/044601.png",use_column_width=True)
        col3.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/077101.png",use_column_width=True)
        st.dataframe(df_min)



    
    

