import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from app_search import run_search_app

def main():
    
    st.title('포켓몬 데이터 분석앱!')

    menu = ['Home','EDA','Search']
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == 'Home':
        run_home_app()
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'Search':
        run_search_app()
        




if __name__ == '__main__':
    main()