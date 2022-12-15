import streamlit as st
import pandas as pd
import numpy as np

def run_search_app():
    df=pd.read_csv('data/pokedex_(Update_05.20).csv')
    df.set_index('pokedex_number',inplace=True)
    df=df.drop(df.columns[0],axis=1)
    df=df.dropna(axis=1)

    poke_word = st.text_input('포켓몬 이름 입력')

    st.text(poke_word)

    df_poke=df[df['name'].str.contains(poke_word,case=False)]

    st.dataframe(df_poke)

    

