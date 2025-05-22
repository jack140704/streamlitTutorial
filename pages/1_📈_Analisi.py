import streamlit as st
from utils.utils import *
import pandas as pd

#ogni tab ha una funzione separata

def create_tab_prodotti(tab_prodotti):
    col1, col2, col3 = tab_prodotti.collums(3)
    #if "connection" in st.session_state.keys():
    payment_info = executeQuery(st.session_state["connection"], "SELECT SUM(amount) AS 'Total Amount', MAX(amount) AS 'Max Payment', AVG(amount) AS 'Average Payment' FROM payments")
    st.write(payment_info)

if __name__ == "__main__":
    st.title("📈 Analisi")

    #creazione dei tab distinti
    tab_prodotti,tab_staff,tab_clienti=st.tabs(["Prodotti","Staff","Clienti"])

    if check_connection():
        pass