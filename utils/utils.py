import streamlit as st
from sqlalchemy import create_engine,text

"""Raccoglie le principali funzioni condivise dalle varie pagine"""

def connect_db(dialect, username, password, host, dbname):
    try:
        engine = create_engine(f"{dialect}://{username}:{password}@{host}/{dbname}")
        conn = engine.connect()
        return conn
    except:
        return False
def check_connection():
    if "connection" not in st.session_state.keys():
        st.session_state["connection"] = False
    
    if st.sidebar.button("Connetti"):
        myconnection = connect_db(dialect="mysql+pymysql", username="student", password="user_pwd", host="localhost", dbname="classicmodels")
        if myconnection is not False:
            st.session_state["connection"] = myconnection
            st.sidebar.success("Connesso")
        else:
            st.session_state["connection"] = False
            st.sidebar.error["Errore connessione db"]