import streamlit as st
from utils.utils import *
import pandas as pd

#ogni tab ha una funzione separata

if __name__ == "__main__":
    st.title("📈 Analisi")

    #creazione dei tab distinti
    tab_prodotti,tab_staff,tab_clienti=st.tabs(["Prodotti","Staff","Clienti"])

    if check_connection():
        pass
    