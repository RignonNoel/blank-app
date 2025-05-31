import streamlit as st
from utils.google_sheet import get_spreadsheet
from gspread.utils import GridRangeType

# Vérifie que la valeur est présente
if "chevre_id" not in st.session_state:
    st.error("Aucun chevre sélectionné.")
    st.stop()

worksheet = get_spreadsheet().sheet1
sheet_content = worksheet.get(return_type=GridRangeType.ListOfLists)

chevre = None
for row in sheet_content:
    if row[0] == st.session_state.chevre_id:
        chevre = row
        break

st.title(f'Chevre: {chevre[0]}')
st.write(f'Nom: {chevre[0]}')
st.write(f'Pere: {chevre[1]}')
st.write(f'Mere: {chevre[2]}')
st.write(f'Sexe: {chevre[3]}')

