import streamlit as st
import pandas as pd
import numpy as np

def run_search_app():
    df=pd.read_csv('data/pokedex_(Update_05.20).csv')
    df.set_index('pokedex_number',inplace=True)
    df=df.drop(df.columns[0],axis=1)
    df=df.dropna(axis=1)

    st.subheader('포켓몬을 검색해보세요!')


    poke_word = st.text_input('포켓몬 이름 입력(영어로)')


    st.text(poke_word)
    
    df_poke=df[df['name'].str.contains(poke_word,case=False)]

    def p_s() : 

            for dex in df_poke.index:
                
                if dex <10:
                        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/000{}01.png".format(dex))
                        
                
                elif dex>10 and dex<100:
                        
                        
                        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/00{}01.png".format(dex))
                        
                

                elif dex>100 and dex<1000:
                        
                        
                        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/0{}01.png".format(dex))
                        
                        
                else:
                    
                        st.image("https://data1.pokemonkorea.co.kr/newdata/pokedex/full/{}01.png".format(dex))
                        

                    
    
    if len(poke_word)!= 0:
        st.dataframe(df_poke)
        p_s()
    else:
        st.info("포켓몬을 검색해보세요")
    
    st.info('영어 이름을 모를땐 포켓몬 도감을 참조하자!')

    st.markdown('https://pokemon.fandom.com/ko/wiki/%EA%B5%AD%EA%B0%80%EB%B3%84_%ED%8F%AC%EC%BC%93%EB%AA%AC_%EC%9D%B4%EB%A6%84_%EB%AA%A9%EB%A1%9D', unsafe_allow_html=True)