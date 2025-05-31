import streamlit as st
import pandas as pd
from utils.google_sheet import get_spreadsheet
from gspread.utils import GridRangeType

st.title("Liste des chèvres")

worksheet = get_spreadsheet().sheet1
sheet_content = worksheet.get(return_type=GridRangeType.ListOfLists)

for data in sheet_content[1:]:
    # Will display 2 columns: one for the name and one 
    # for a button, with 3 spaces and 1 space respectively
    col1, col2 = st.columns([3, 1])

    col1.write(data[0])

    if col2.button("Voir profil", key=data[0]):
        st.session_state["chevre_id"] = data[0]
        st.switch_page("pages/detail_chevre.py")