import streamlit as st
import pandas as pd
import os

def display_raw_page():

    st.header("voici vos fichier télécharger")

    # Correspondance entre choix utilisateur et fichiers existants
    files = {
        "Chiens": "data/chiens_scraped.csv",
        "Moutons": "data/moutons_scraped.csv",
        "Poules - Lapins - Pigeons": "data/poules-lapins-et-pigeons_scraped.csv",
        "Autres animaux": "data/autres-animaux_scraped.csv"
    }

    choice = st.selectbox("Choisir un fichier :", list(files.keys()))

    filepath = files[choice]

    # Vérifier l'existence du fichier
    if not os.path.exists(filepath):
        st.error(f"Le fichier sélectionné n'existe pas : {filepath}")
        return

    df = pd.read_csv(filepath)
    st.dataframe(df)
