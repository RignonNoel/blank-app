import streamlit as st
from utils.encrypt import decrypt_file, encrypt_file

st.title("Bienvenue sur mon app !")

with st.form("login_form"):
    password = st.text_input("Mot de passe")

    if st.form_submit_button("Se connecter"):

        try:
            decrypt_file("credentials.enc", "credentials.json", password)
            st.success("Connexion réussie !")
            st.switch_page("pages/liste_chevres.py")
        except:
            st.error("Mot de passe incorrect.")
        
        

