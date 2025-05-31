import streamlit as st
from utils.google_sheet import get_spreadsheet

st.title("Ajouter une chèvre")

with st.form("formulaire"):
    nom = st.text_input("Nom")
    age = st.number_input("Âge", min_value=0, max_value=120, step=1)
    submitted = st.form_submit_button("Soumettre")

if submitted:
    if nom.strip():
        worksheet = get_spreadsheet().sheet1
        worksheet.append_row([nom, age])
        st.success("Enregistré avec succès !")
    else:
        st.error("Le nom ne peut pas être vide.")
